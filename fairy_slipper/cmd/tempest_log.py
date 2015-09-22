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


def parse_logfile(log_file):
    """Yet another shonky stream parser."""
    calls = []
    current_request = {}
    current_response = {}
    content_length = 0
    for line in log_file:
        if RUBBISH_LINE_RE.match(line):
            continue
        request = REQUEST_RE.match(line)
        if request:
            if current_request and current_response:
                calls.append((current_request, current_response))
            request_dict = request.groupdict()
            url = urlparse.urlsplit(request_dict['url'])
            port = url.netloc.split(':')[-1]
            service = DEFAULT_PORTS[port]
            current_request = {
                'service': service,
                'url': urlparse.urlunsplit(('', '') + url[2:]),
                'method': request_dict['method']}
            current_response = {
                'status_code': request_dict['status_code']}
        else:
            start_request = REQUEST1_RE.match(line)
            if start_request:
                line = re.sub(PYTHON_LOG_PREFIX_RE, '', line)
            try:
                key, value = line.split(':', 1)
            except ValueError:
                # For some wacky reason, when you request JSON,
                # sometimes you get text.  Handle this rad behaviour.
                if current_response.get('headers') is not None:
                    try:
                        current_response['body'] += line
                    except:
                        print(line)
                        continue
                else:
                    try:
                        current_request['body'] += line
                    except:
                        print(line)
                        continue
                continue
            key = key.strip()
            value = value.strip()
            if key == 'Request - Headers':
                current_request['headers'] = {k.lower(): v
                                              for k, v in eval(value).items()}
                res_or_req = current_request
                content_length = int(current_request['headers']
                                     .get('content-length', 0))
            if key == 'Response - Headers':
                current_response['headers'] = {k.lower(): v
                                               for k, v in eval(value).items()}
                res_or_req = current_response
                content_length = int(current_response['headers']
                                     .get('content-length', 0))
            if key == 'Body':
                if content_length == 0:
                    body = None
                elif value[:4] == 'None':
                    body = None
                elif 'application/json' == res_or_req.get('content-type'):
                    if '_log_request_full' in value:
                        value = value.split('_log_request_full')[0]
                    try:
                        body = json.loads(value)
                        body = json.dumps(body, indent=2,
                                          sort_keys=True,
                                          separators=(',', ': '))
                        continue
                    except ValueError:
                        body = value

                        log.warning("Headers %r", res_or_req)
                        log.warning("Failed to parse %r", value)
                else:
                    body = value

                res_or_req['body'] = body
    else:
        calls.append((current_request, current_response))
    return calls


def main1(log_file, output_dir):
    log.info('Reading %s' % log_file)
    calls = parse_logfile(open(log_file))
    services = defaultdict(list)
    for call in calls:
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
