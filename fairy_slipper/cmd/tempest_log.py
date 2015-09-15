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
import urlparse

log = logging.getLogger(__name__)

DEFAULT_PORTS = {
    '5000': 'identity',
    '35357': 'identity-admin',
    '8774': 'compute',
    '8776': 'volume',
    '8773': 'compute-ec2',
    '9292': 'image',
}
REQUEST_RE = re.compile("Request (?P<test>\([^()]+\)):"
                        " (?P<status_code>\d+)"
                        " (?P<method>[A-Z]+) (?P<url>\S+)")


def parse_logfile(log_file):
    """Yet another shonky stream parser."""
    calls = []
    current_request = {}
    current_response = {}
    for line in log_file:
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
            try:
                key, value = line.split(':', 1)
            except ValueError:
                # For some wacky reason, when you request JSON,
                # sometimes you get text.  Handle this rad behaviour.
                if current_response.get('headers') is not None:
                    current_response['body'] += line
                else:
                    current_request['body'] += line
                continue
            key = key.strip()
            value = value.strip()
            if key == 'Request - Headers':
                current_request['headers'] = eval(value)
            if key == 'Response - Headers':
                current_response['headers'] = eval(value)
            if key == 'Body':
                if value == 'None':
                    body = None
                elif value == '':
                    body = None
                else:
                    try:
                        body = json.loads(value)
                        body = json.dumps(body, indent=2, sort_keys=True)
                    except ValueError:
                        body = value
                        log.info("Failed to parse %r", value)
                if current_response.get('headers') is not None:
                    current_response['body'] = body
                else:
                    current_request['body'] = body
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
