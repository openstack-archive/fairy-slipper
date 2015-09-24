# Copyright (c) 2015 Russell Sim <russell.sim@gmail.com>
#
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
from __future__ import unicode_literals

from collections import defaultdict
import json
import logging
from os import path
import re
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

log = logging.getLogger(__name__)

DEFAULT_PORTS = {
    '5000': 'identity',
    '35357': 'identity-admin',
    '8774': 'compute',
    '8776': 'volume',
    '8773': 'compute-ec2',
    '9292': 'image',
    '9696': 'networking',
    '9292': 'image',
    '8082': 'application-catalog',
    '8004': 'orchestration',
    '8080': 'object',
    '8777': 'telemetry',
}

PYTHON_LOG_PREFIX_RE = ("^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}) \d+ "
                        "(?P<log_level>[A-Z]+) (?P<logger_name>\S+) "
                        "\[(?P<tags>[^\[\]]+)\] ")

REQUEST_RE = re.compile(PYTHON_LOG_PREFIX_RE + "Request (?P<test>\([^()]+\)):"
                        " (?P<status_code>\d+)"
                        " (?P<method>[A-Z]+) (?P<url>\S+)")

REQUEST1_RE = re.compile(PYTHON_LOG_PREFIX_RE + "Request")

RUBBISH_LINE_RE = re.compile("^    _log_request_full \S+:\d+$")

REQ_RE = re.compile('(req-[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}'
                    '-[a-z0-9]{4}-[a-z0-9]{12})')


class DB(object):

    def __init__(self):
        self.requests = {}
        self.responses = {}

    def _normalize_headers(self, headers):
        return {k.lower(): v for k, v in headers.items()}

    def create(self, req, request):
        url = urlparse.urlsplit(request['url'])
        port = url.netloc.split(':')[-1]
        service = DEFAULT_PORTS[port]

        self.requests[req] = {
            'service': service,
            'url': urlparse.urlunsplit(('', '') + url[2:]),
            'method': request['method']}
        self.responses[req] = {
            'status_code': request['status_code']}

    def set_request_headers(self, req, headers):
        self.requests[req]['headers'] = self._normalize_headers(headers)

    def set_response_headers(self, req, headers):
        self.responses[req]['headers'] = self._normalize_headers(headers)

    def get_req_or_resp_length(self, req):
        if self.responses[req].get('headers') is not None:
            return int(self.responses[req]['headers'].get('content-length', 0))
        else:
            return int(self.requests[req]['headers'].get('content-length', 0))

    def get_req_or_resp_content_type(self, req):
        if self.responses[req].get('headers') is not None:
            return self.responses[req]['headers'].get('content-type',
                                                      'text/plain')
        else:
            return self.requests[req]['headers'].get('content-type',
                                                     'text/plain')

    def append_req_or_resp_body(self, req_id, string):
        if self.responses[req_id].get('headers') is not None:
            self.responses[req_id]['body'] += string
        else:
            self.requests[req_id]['body'] += string

    def set_req_or_resp_body(self, req_id, string):
        if self.responses[req_id].get('headers') is not None:
            self.responses[req_id]['body'] = string
        else:
            self.requests[req_id]['body'] = string


def parse_logfile(log_file):
    """Yet another shonky stream parser."""
    content_length = 0
    current_req_id = ''
    db = DB()
    for line in log_file:
        if RUBBISH_LINE_RE.match(line):
            continue
        request = REQUEST_RE.match(line)
        if request:
            request_dict = request.groupdict()
            try:
                current_req_id = REQ_RE.match(request_dict['tags']).groups()[0]
            except AttributeError:
                # Swift calls don't have the req tag
                current_req_id = ''
            if current_req_id:
                db.create(current_req_id, request_dict)
        else:
            start_request = REQUEST1_RE.match(line)
            if start_request:
                line = re.sub(PYTHON_LOG_PREFIX_RE, '', line)
                try:
                    current_req_id = REQ_RE.match(
                        start_request.groupdict()['tags']).groups()[0]
                except AttributeError:
                    # Swift calls don't have the req tag
                    current_req_id = ''

                # Skip all boto logs
                if 'boto' == start_request.groupdict()['logger_name']:
                    current_req_id = ''
            try:
                key, value = line.split(':', 1)
            except ValueError:
                # For some wacky reason, when you request JSON,
                # sometimes you get text.  Handle this rad behaviour.
                if not current_req_id:
                    continue

                try:
                    db.append_req_or_resp_body(current_req_id, line)
                except TypeError:
                    log.warning('Failed to find body to add to.')
                continue

            key = key.strip()
            value = value.strip()

            if key == 'Request - Headers':
                if current_req_id:
                    db.set_request_headers(current_req_id, eval(value))
            if key == 'Response - Headers':
                if current_req_id:
                    db.set_response_headers(current_req_id, eval(value))
            if key == 'Body':
                if not current_req_id:
                    continue

                content_length = db.get_req_or_resp_length(current_req_id)
                content_type = db.get_req_or_resp_content_type(current_req_id)

                # Trim any messages that are by accident on the end of
                # the line
                if '_log_request_full' in value:
                    value = value.split('_log_request_full')[0]

                if content_length == 0:
                    body = None
                elif value[:4] == 'None':
                    body = None
                elif 'application/json' in content_type:
                    try:
                        body = json.loads(value)
                        body = json.dumps(body, indent=2,
                                          sort_keys=True,
                                          separators=(',', ': '))
                    except ValueError:
                        body = value
                        log.warning("Failed to parse %r", value)
                else:
                    body = value
                db.set_req_or_resp_body(current_req_id, body)
    return db


def main1(log_file, output_dir):
    log.info('Reading %s' % log_file)
    calls = parse_logfile(open(log_file))
    services = defaultdict(list)
    for req in calls.requests:
        call = (calls.requests[req], calls.responses[req])
        services[call[0]['service']].append(call)
    for service, calls in services.items():
        pathname = path.join(output_dir, '%s-examples.json' % (service))
        with open(pathname, 'w') as out_file:
            json.dump(calls, out_file, indent=2)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help="Increase verbosity (specify multiple times for more)")
    parser.add_argument(
        '-o', '--output-dir', action='store',
        help="The directory to output the JSON files too.")
    parser.add_argument(
        'filename',
        help="File to convert")

    args = parser.parse_args()

    log_level = logging.WARNING
    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s %(name)s %(levelname)s %(message)s')

    filename = path.abspath(args.filename)

    main1(filename, output_dir=args.output_dir)
