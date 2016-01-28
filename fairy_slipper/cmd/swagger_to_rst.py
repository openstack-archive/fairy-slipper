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

import codecs
import json
import logging
import os
from os import path
import textwrap

from jinja2 import Environment

log = logging.getLogger(__name__)

TMPL_TAG = """
{%- for tag in swagger.tags -%}

.. swagger:tag:: {{tag.name}}
   :synopsis: {{tag.description}}
{% for line in tag['x-summary'].split('\n') %}
   {{line}}
{%- endfor %}

{% endfor %}
"""

TMPL_API = """
{%- for path, methods in swagger['paths'].items() -%}
{%- for method_name, request in methods.items() -%}

.. http:{{method_name}}:: {{path}}
   :title: {{request['x-title']}}
   :synopsis: {{request['summary']}}
{%- if request.description != '' %}
{% for line in request.description.split('\n') %}
   {{line}}
{%- endfor %}
{%- endif %}
{% for status_code, response in request.responses.items() %}
{%- if response['examples']['application/json'] %}
   :responseexample {{status_code}}: {{version}}/examples/{{request['operationId']}}_resp_{{status_code}}.json
{%- endif -%}
{%- if response['examples']['text/plain'] %}
   :responseexample {{status_code}}: {{version}}/examples/{{request['operationId']}}_resp_{{status_code}}.txt
{%- endif -%}
{%- if response['schema']['$ref'] %}
   :responseschema {{status_code}}: {{version}}/{{response['schema']['$ref'].rsplit('/', 1)[1]}}.json
{%- endif -%}
{% endfor -%}
{% for mime in request.consumes %}
   :accepts: {{mime}}
{%- endfor -%}
{% for mime in request.produces %}
   :produces: {{mime}}
{%- endfor -%}
{% for tag in request.tags %}
   :tag: {{tag}}
{%- endfor -%}
{% for parameter in request.parameters -%}
{% if parameter.in == 'body' -%}
{% if parameter.schema %}
   :requestschema: {{version}}/{{request['operationId']}}.json
{%- for id, schema in swagger['definitions'].items() -%}
{%- if id == request['operationId'] -%}
{%- if 'example' in schema -%}
{%- if schema['example']['application/json'] %}
   :requestexample: {{version}}/examples/{{request['operationId']}}_req.json
{%- endif -%}
{%- if schema['example']['text/plain'] %}
   :requestexample: {{version}}/examples/{{request['operationId']}}_req.txt
{%- endif -%}
{%- endif -%}
{%- endif -%}
{%- endfor -%}
{%- endif -%}
{%- elif parameter.in == 'path' %}
{{ parameter|format_param('parameter') }}
{%- elif parameter.in == 'query' %}
{{ parameter|format_param('query') }}
{%- elif parameter.in == 'header' %}
{{ parameter|format_param('reqheader') }}
{%- endif %}
{%- endfor -%}
{% for status_code, response in request['responses'].items() %}
   :statuscode {{status_code}}: {{response.description}}
{%- endfor %}


{% endfor %}
{%- endfor %}
"""  # noqa

environment = Environment()


def format_param(obj, type='query'):
    param = '   :%s %s: ' % (type, obj['name'])
    param_wrap = textwrap.TextWrapper(
        initial_indent=param,
        subsequent_indent=' ' * len(param))
    if ('::\n\n' in obj['description']) or \
       ('.. code-block::' in obj['description']):
        param_len = len(param)
        for i, line in enumerate(obj['description'].split('\n')):
            if i is 0:
                param += line + '\n'
            else:
                param += ' ' * param_len + line + '\n'
        return param
    else:
        new_text = param_wrap.wrap(obj['description'])
        return '\n'.join(new_text)


environment.filters['format_param'] = format_param


def main1(filename, output_dir):
    log.info('Parsing %s' % filename)
    swagger = json.load(open(filename))
    write_rst(swagger, output_dir)
    write_jsonschema(swagger, output_dir)
    write_examples(swagger, output_dir)
    write_index(swagger, output_dir)


def write_index(swagger, output_dir):
    info = swagger['info']
    service = info['x-service']

    # Web UI uses 'service' field for indexing
    del info['x-service']
    info['service'] = service
    version = info['version']
    output_file = 'index.json'
    filepath = path.join(output_dir, output_file)
    log.info("Writing APIs %s", filepath)
    if path.exists(filepath):
        index = json.load(open(filepath))
    else:
        index = {}
    index['/'.join([service, version, ''])] = info
    with codecs.open(filepath,
                     'w', "utf-8") as out_file:
        json.dump(index, out_file, indent=2)


def write_rst(swagger, output_dir):
    environment.extend(swagger_info=swagger['info'])
    write_apis(swagger, output_dir)
    write_tags(swagger, output_dir)


def write_apis(swagger, output_dir):
    info = swagger['info']
    version = info['version']
    service = info['x-service']
    service_path = path.join(output_dir, service)
    output_file = '%s.rst' % version
    if not path.exists(service_path):
        os.makedirs(service_path)
    TMPL = environment.from_string(TMPL_API)
    result = TMPL.render(swagger=swagger,
                         version=swagger['info']['version'])
    filepath = path.join(service_path, output_file)
    log.info("Writing APIs %s", filepath)
    with codecs.open(filepath,
                     'w', "utf-8") as out_file:
        out_file.write(result)


def write_tags(swagger, output_dir):
    info = swagger['info']
    version = info['version']
    service = info['x-service']
    service_path = path.join(output_dir, service)
    if not path.exists(service_path):
        os.makedirs(service_path)
    output_file = '%s-tags.rst' % version
    TMPL = environment.from_string(TMPL_TAG)
    result = TMPL.render(swagger=swagger,
                         version=swagger['info']['version'])
    filepath = path.join(service_path, output_file)
    log.info("Writing Tags %s", filepath)
    with codecs.open(filepath,
                     'w', "utf-8") as out_file:
        out_file.write(result)


def write_jsonschema(swagger, output_dir):
    info = swagger['info']
    version = info['version']
    service = info['x-service']
    service_path = path.join(output_dir, service)
    full_path = path.join(service_path, version)
    if not path.exists(service_path):
        os.makedirs(service_path)
    if not path.exists(full_path):
        os.makedirs(full_path)

    for schema_name, schema in swagger['definitions'].items():
        filename = '%s.json' % schema_name
        filepath = path.join(full_path, filename)
        log.info("Writing %s", filepath)
        file = open(filepath, 'w')
        json.dump(schema, file, indent=2)


def write_examples(swagger, output_dir):
    info = swagger['info']
    version = info['version']
    service = info['x-service']
    service_path = path.join(output_dir, service)
    versioned_path = path.join(service_path, version)
    full_path = path.join(versioned_path, 'examples')
    if not path.exists(service_path):
        os.makedirs(service_path)
    if not path.exists(versioned_path):
        os.makedirs(versioned_path)
    if not path.exists(full_path):
        os.makedirs(full_path)

    for paths in swagger['paths'].values():
        for operation in paths.values():
            for status_code, response in operation['responses'].items():
                for mime, example in response['examples'].items():
                    filename = '%s' % '_'.join([operation['operationId'],
                                                'resp',
                                                status_code])
                    if mime == 'application/json':
                        filepath = path.join(full_path, filename + '.json')
                        log.info("Writing %s", filepath)
                        file = open(filepath, 'w')
                        json.dump(example, file, indent=2)
                    if mime == 'text/plain':
                        filepath = path.join(full_path, filename + '.txt')
                        log.info("Writing %s", filepath)
                        example = example.strip()
                        example = example + '\n'
                        file = open(filepath, 'w')
                        file.write(example)

    for ids, schemas in swagger['definitions'].items():
        if 'example' in schemas:
            for mime, example in schemas['example'].items():
                filename = '%s' % '_'.join(
                    [ids, 'req'])
                if mime == 'application/json':
                    filepath = path.join(full_path, filename + '.json')
                    log.info("Writing %s", filepath)
                    file = open(filepath, 'w')
                    json.dump(example, file, indent=2)
                if mime == 'text/plain':
                    filepath = path.join(full_path, filename + '.txt')
                    log.info("Writing %s", filepath)
                    example = example.strip()
                    example = example + '\n'
                    file = open(filepath, 'w')
                    file.write(example)


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
