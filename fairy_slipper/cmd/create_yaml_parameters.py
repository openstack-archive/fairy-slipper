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

import codecs
from jinja2 import Environment
import json
import logging
import os
from os import path
import textwrap
import yaml


log = logging.getLogger(__name__)
environment = Environment()


TMPL_API = """
{{method['title']}}
{% for i in range(method['title']|count) -%}
=
{%- endfor %}

.. rest_method::  {{method['method']|upper}} {{path}}

{{method['summary']}}

{%- if method.description != '' %}
{% for line in method.description.split('\n') %}
{{line}}
{%- endfor %}
{%- endif %}

{% for status_code, response in method['responses'].items() %}
{%- if status_code == '200' %}
Normal response codes: {{status_code}}
{% endif -%}
{%- endfor -%}


Error response codes:
{%- for status_code in error_codes -%}
{{status_code}},
{%- endfor %}


Request Parameters
------------------

.. rest_parameters:: {{method['operationId']}}.yaml
{% for p in request_params %}
   - {{p}}: {{p}}
{%- endfor %}

{%- if 'application/json' in method['examples'] %}

Request Example
---------------

.. literalinclude:: {{method['request_sample']}}
   :language: javascript
{% endif %}


{% if response_params|count > 0 %}
Response Parameters
-------------------

.. rest_parameters:: {{method['operationId']}}.yaml
{% for p in response_params %}
   - {{p}}: {{p}}
{%- endfor %}
{% endif %}


{% for status_code, response in method['responses'].items() %}
{%- if status_code == '200' %}
Response Example
----------------

.. literalinclude:: {{response['response_sample']}}
   :language: javascript

{% endif %}
{% endfor %}

"""


def create_parameter(name, form, request, opt, ptype):
    p = {}
    p[name] = {}
    if form is not '':
        p[name]['format'] = form
    p[name]['in'] = request
    p[name]['required'] = opt
    p[name]['type'] = ptype
    return p


def format_param(desc):
    desc.rstrip('\n')
    param = '  description: |\n'
    param_wrap = textwrap.TextWrapper(
        initial_indent=param,
        subsequent_indent='    ')
    if ('::\n\n' in desc) or \
       ('.. code-block::' in desc):
        for i, line in enumerate(desc.split('\n')):
            if len(line) is 0:
                param += '\n'
            else:
                param += '    ' + line + '\n'
        return param.rstrip('\n')
    else:
        new_text = param_wrap.wrap('    ' + desc)
        return '\n'.join(new_text)


def main1(filename, output_dir):
    log.info('Parsing %s' % filename)
    swagger = json.load(open(filename))

    info = swagger['info']
    version = info['version']
    service = info['service']
    service_path = path.join(output_dir, service)
    full_path = path.join(service_path, version)
    if not path.exists(service_path):
        os.makedirs(service_path)
    if not path.exists(full_path):
        os.makedirs(full_path)

    # Create .inc files for each tag
    for tags in swagger['tags']:
        filename_rst = ""
        if 'name' in tags and tags['name'] is not "":
            filename_rst = '%s.inc' % tags['name']
        filepath_rst = path.join(full_path, filename_rst)

        log.info("Writing RST inc file %s", filepath_rst)
        with codecs.open(filepath_rst,
                         'w', "utf-8") as out_file:
            out_file.write(".. -*- rst -*-\n\n")
            out_file.write('=' * len(tags['description']))
            out_file.write("\n")
            out_file.write(tags['description'])
            out_file.write("\n")
            out_file.write('=' * len(tags['description']))
            out_file.write("\n\n")
            out_file.write(tags['summary'])
            out_file.write("\n\n")

    for key_path, paths in swagger['paths'].items():
        for p in paths:
            opId = p['operationId']
            method_req_params = p['parameters']
            tag = p['tags'][0]
            request_params = []
            response_params = []

            filename = '%s.yaml' % opId
            filepath = path.join(full_path, filename)
            log.info("Writing %s", filepath)
            stream = file(filepath, 'a')

            # get the response objects
            method_responses = p['responses']
            for r, rval in method_responses.items():
                if 'headers' in rval:
                    for h, val in rval['headers'].items():
                        new_param = create_parameter(h,
                                                     val['format'],
                                                     str('header'),
                                                     val['required'],
                                                     val['type'])

                        response_params.append(h)
                        yaml.safe_dump(new_param,
                                       stream,
                                       allow_unicode=True,
                                       default_flow_style=False)
                        new_desc = format_param(val['description'])
                        stream.write(new_desc.encode('utf8'))
                        stream.write('\n\n')

                # get the response parameters
                if 'schema' in rval:
                    response_schema_name = opId + '_' + r
                    for op, opval in swagger['definitions'].items():
                        if op == response_schema_name:
                            props = opval['properties']
                            for k, val in props.items():
                                new_param = create_parameter(k,
                                                             val['format'],
                                                             str("body"),
                                                             val['required'],
                                                             val['type'])

                                # add to response param list
                                response_params.append(k)

                                yaml.safe_dump(new_param,
                                               stream,
                                               allow_unicode=True,
                                               default_flow_style=False)
                                new_desc = format_param(val['description'])
                                stream.write(new_desc.encode('utf8'))
                                stream.write('\n\n')

            # get the request parameters
            for params in method_req_params:
                if params['in'] == 'body':
                    for op, opval in swagger['definitions'].items():
                        if op == opId:
                            props = opval['properties']
                            for k, val in props.items():
                                new_param = create_parameter(k,
                                                             val['format'],
                                                             str("body"),
                                                             val['required'],
                                                             val['type'])

                                # add to request param list
                                request_params.append(k)

                                yaml.safe_dump(new_param,
                                               stream,
                                               allow_unicode=True,
                                               default_flow_style=False)
                                new_desc = format_param(val['description'])
                                stream.write(new_desc.encode('utf8'))
                                stream.write('\n\n')

                else:
                    new_param = create_parameter(params['name'],
                                                 params['format'],
                                                 params['in'],
                                                 params['required'],
                                                 params['type'])
                    # add to request param list
                    request_params.append(params['name'])

                    yaml.safe_dump(new_param,
                                   stream,
                                   allow_unicode=True,
                                   default_flow_style=False)
                    new_desc = format_param(params['description'])
                    stream.write(new_desc.encode('utf8'))
                    stream.write('\n\n')

            # error responses
            error_codes = []
            for status_code in p['responses']:
                if status_code > '200':
                    error_codes.append(status_code)

            TMPL = environment.from_string(TMPL_API)
            result = TMPL.render(method=p,
                                 path=key_path,
                                 request_params=request_params,
                                 response_params=response_params,
                                 error_codes=error_codes)

            # Append method info to inc file
            filename_rst = '%s.inc' % tag
            filepath_rst = path.join(full_path, filename_rst)

            log.info("Writing RST inc file %s", filepath_rst)
            with codecs.open(filepath_rst,
                             "a", "utf-8") as out_file:
                out_file.write(result)

            # write out a rst file
            filename_rst = '%s.rst' % opId
            filepath_rst = path.join(full_path, filename_rst)
            log.info("Writing RST/operation %s", filepath_rst)
            with codecs.open(filepath_rst,
                             'w', "utf-8") as out_file:
                out_file.write(result)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help="Increase verbosity (specify multiple times for more)")
    parser.add_argument(
        '-o', '--output-dir', action='store',
        help="The directory where the yaml files will be output.")
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
