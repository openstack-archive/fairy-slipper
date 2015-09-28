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
from copy import copy
import json
import logging
import os
from os import path
import re
import textwrap
import xml.sax

from jinja2 import Environment
import prettytable

log = logging.getLogger(__name__)

TYPE_MAP = {
    'string': 'string',
    'xsd:string': 'string',
    'csapi:string': 'string',
    'xsd:int': 'integer',
    'csapi:uuid': 'string',
    'xsd:boolean': 'boolean',
    'boolean': 'boolean',
    'object': 'object',
    'csapi:bool': 'boolean',
    'xsd:bool': 'boolean',
    'xsd:datetime': 'string',
    'regexp': 'string',
    'xsd:datetime': 'string',
    'xsd:dict': 'object',
    'alarm': 'string',
    'xsd:timestamp': 'string',
    'xsd:char': 'string',
    'list': 'array',
    'csapi:flavorswithonlyidsnameslinks': 'string',
    'csapi:imagestatus': 'string',
    'csapi:imageswithonlyidsnameslinks': 'string',
    'xsd:enum': 'string',
    'xsd:anyuri': 'string',
    'csapi:serverforupdate': 'string',
    'capi:uuid': 'string',
    'xsd:uuid': 'string',
    'string': 'string',
    'imageapi:string': 'string',
    'imageapi:imagestatus': 'string',
    'imageapi:uuid': 'string',
    'csapi:uuid': 'string',
    'csapi:serverforcreate': 'string',
    'csapi:blockdevicemapping': 'string',
    'csapi:serverswithonlyidsnameslinks': 'string',
    'csapi:serverstatus': 'string',
    'csapi:dict': 'object',
    'imageforcreate': 'string',
    'xsd:ip': 'string',
    'xsd:base64binary': 'string',

    # TODO(arrsim) This array types also set the items
    # "tags": {
    #    "type": "array",
    #    "items": {
    #        "type": "string"
    'xsd:list': 'array',
    'array': 'array',
}

FORMAT_MAP = {
    'xsd:anyURI': 'uri',
    'xsd:datetime': 'date-time',
    'xsd:ip': 'ipv4',
    'regexp': 'regexp',
    'xsd:timestamp': 'timestamp',
}

STYLE_MAP = {
    'template': 'path',
    'plain': 'body',
    'query': 'query',
    'header': 'header',
}

MIME_MAP = {
    'json': 'application/json',
    'txt': 'text/plain',
    'xml': 'application/xml',
}

VERSION_RE = re.compile('v[0-9\.]+')
WHITESPACE_RE = re.compile('[\s]+', re.MULTILINE)
URL_TEMPLATE_RE = re.compile('{[^{}]+}')

environment = Environment()
HTTP_REQUEST = """{{ method }} {{ url }} HTTP/1.1
{% for key, value in headers.items() -%}
{{ key }}: {{ value }}
{% endfor %}
"""
HTTP_REQUEST_TMPL = environment.from_string(HTTP_REQUEST)

HTTP_RESPONSE = """HTTP/1.1 {{ status_code }}
{% for key, value in headers.items() -%}
{{ key }}: {{ value }}
{% endfor %}
{{ body }}
"""
HTTP_RESPONSE_TMPL = environment.from_string(HTTP_RESPONSE)


def create_parameter(name, _in, description='',
                     type='xsd:string', required=True):
    return {
        "name": name,
        "in": STYLE_MAP[_in],
        "description": description,
        "required": True if required == 'true' else False,
        "type": TYPE_MAP[type.lower()],
        "format": FORMAT_MAP.get(type, ''),
    }


def join_url(parts):
    """Return a joined url without any duplicate slashes"""
    return '/'.join(parts).replace('//', '/')


class SubParser(xml.sax.ContentHandler):
    def __init__(self, parent):
        # general state
        self.tag_stack = []
        self.attr_stack = []
        self.parent = parent
        self.result = None
        self.kwargs = {}

    def startElement(self, name, _attrs):
        attrs = dict(_attrs)
        self.tag_stack.append(name)
        self.attr_stack.append(attrs)
        return attrs

    def endElement(self, name):
        self.tag_stack.pop()
        self.attr_stack.pop()
        if not self.tag_stack:
            self.parent.detach_subparser(self.result, **self.kwargs)

    def search_stack_for(self, tag_name):
        for tag, attrs in zip(reversed(self.tag_stack),
                              reversed(self.attr_stack)):
            if tag == tag_name:
                return attrs

    def on_top_tag_stack(self, *args):
        return self.tag_stack[-len(args):] == list(args)


class TableMixin(object):
    def visit_table(self, attrs):
        self.__table = prettytable.PrettyTable(hrules=prettytable.ALL)
        self.__table.header = False

    def depart_table(self):
        self.content.append('\n\n')
        self.content.append(str(self.__table))
        self.content.append('\n\n')

    # TODO(Karen)
    def visit_caption(self, attrs):
        pass

    def depart_caption(self):
        pass

    def visit_th(self, attrs):
        self.__table.header = True

    def depart_th(self):
        heading = self.content.pop().strip()
        self.__table.field_names.append(heading)
        self.__table.align[heading] = 'l'
        self.__table.valign[heading] = 't'
        self.__table.max_width[heading] = 80

    def visit_tr(self, attrs):
        self.__row = []

    def visit_td(self, attrs):
        self.content_stack.append([])

    def depart_td(self):
        self.__row.append(''.join(self.content_stack.pop()).strip())

    def depart_tr(self):
        if self.__row:
            columns = len(self.__table.field_names)
            self.__row.extend(['' for n in range(columns - len(self.__row))])
            self.__table.add_row(self.__row)


class ParaParser(SubParser, TableMixin):

    EMPHASIS = {
        'bold': '**',
        'italic': '*'
    }

    def __init__(self, parent):
        super(ParaParser, self).__init__(parent)
        self.content_stack = [[]]
        self.current_emphasis = None
        self.nesting = 0
        self.no_space = False
        self.fill_width = 67
        self.wrapper = textwrap.TextWrapper(width=self.fill_width)
        self.shortdesc = False
        self.inline_markup_stack = []
        self.hyperlink_end = False

    @property
    def content(self):
        return self.content_stack[-1]

    def startElement(self, name, _attrs):
        super(ParaParser, self).startElement(name, _attrs)
        fn = getattr(self, 'visit_%s' % name, None)
        if fn:
            fn(dict(_attrs))

    def endElement(self, name):
        content = ''.join(self.content)
        self.result = content
        super(ParaParser, self).endElement(name)
        fn = getattr(self, 'depart_%s' % name, None)
        if fn:
            fn()

    def characters(self, content):
        if not content:
            return
        # Fold up any white space into a single char
        if not self.on_top_tag_stack('programlisting'):
            content = WHITESPACE_RE.sub(' ', content)

        if content == ' ':
            return
        if content[0] == '\n':
            return
        if self.content:
            if self.content[-1].endswith('\n'):
                content = ' ' * self.nesting + content.strip()
            elif self.content[-1].endswith(' '):
                content = content.strip()
            elif (self.on_top_tag_stack('programlisting')):
                content = '\n' + ' ' * self.nesting + content
            elif self.no_space:
                content = '' + content.strip()
            elif self.hyperlink_end and content == '.':
                self.hyperlink_end = False
            else:
                content = ' ' + content.strip()

        if self.no_space is True:
            self.inline_markup_stack.append(content)
        else:
            self.content.append(content)

    def visit_listitem(self, attrs):
        self.nesting = len([tag for tag in self.tag_stack
                            if tag == 'listitem']) - 1
        self.content_stack.append([' ' * self.nesting + '-'])
        self.wrapper = textwrap.TextWrapper(
            width=self.fill_width,
            initial_indent=' ',
            subsequent_indent=' ' * self.nesting + '  ',)

    def depart_listitem(self):
        content = self.content_stack.pop()
        self.content.append(''.join(content))
        self.content.append('\n')

        self.nesting = len([tag for tag in self.tag_stack
                            if tag == 'listitem'])

    def depart_itemizedlist(self):
        if self.search_stack_for('itemizedlist') is None:
            self.wrapper = textwrap.TextWrapper(width=self.fill_width)

    def depart_orderedlist(self):
        if self.search_stack_for('itemizedlist') is None:
            self.wrapper = textwrap.TextWrapper(width=self.fill_width)

    def visit_para(self, attrs):
        if attrs.get('role') == 'shortdesc':
            self.shortdesc = True
        self.content_stack.append([''])
        if self.search_stack_for('itemizedlist') is not None:
            return
        if self.content:
            if self.content[-1].endswith('\n\n'):
                pass
            elif self.content[-1].endswith('\n'):
                self.content.append('\n')

    def depart_para(self):
        content = ''.join(self.content_stack.pop()).strip()
        wrapped = self.wrapper.wrap(content)
        self.content.append('\n'.join(wrapped))
        if self.search_stack_for('itemizedlist') is None:
            self.content.append('\n\n')
        else:
            self.content.append('\n')
            self.wrapper = textwrap.TextWrapper(
                width=self.fill_width,
                initial_indent=' ' * self.nesting + '  ',
                subsequent_indent=' ' * self.nesting + '  ',)
        if self.shortdesc is True:
            self.kwargs['shortdesc'] = self.result.strip()
            # Reset state variables
            self.content_stack = [[]]
            self.shortdesc = False

    def visit_title(self, attrs):
        self.current_emphasis = attrs.get('role', 'bold')
        self.no_space = True

    def depart_title(self):
        content = ' ' + self.EMPHASIS[self.current_emphasis]
        content += ' '.join(self.inline_markup_stack[0:None])
        content += self.EMPHASIS[self.current_emphasis]
        self.content.append(content)
        self.content.append('\n\n')
        self.inline_markup_stack[:] = []
        self.no_space = False
        self.current_emphasis = None

    def visit_code(self, attrs):
        self.no_space = True

    def depart_code(self):
        content = ' ``'
        content += ' '.join(self.inline_markup_stack[0:None])
        content += '``'
        self.content.append(content)
        self.inline_markup_stack[:] = []
        self.no_space = False

    def visit_emphasis(self, attrs):
        # Bold is the default emphasis
        self.current_emphasis = attrs.get('role', 'bold')
        self.no_space = True

    def depart_emphasis(self):
        content = ' ' + self.EMPHASIS[self.current_emphasis]
        content += ' '.join(self.inline_markup_stack[0:None])
        content += self.EMPHASIS[self.current_emphasis]
        self.content.append(content)
        self.inline_markup_stack[:] = []
        self.no_space = False
        self.current_emphasis = None

    def visit_programlisting(self, attrs):
        if not attrs:
            self.content.append('::\n\n')
        else:
            self.content.append('.. code-block:: %s\n\n' % attrs['language'])
        self.nesting = 3

    def depart_programlisting(self):
        self.nesting = 0  # no indent for blank lines
        self.content.append('\n\n')

    def visit_link(self, attrs):
        if attrs:
            self.inline_markup_stack.append(attrs['xlink:href'])
            self.no_space = True

    def depart_link(self):
        content = ' `'
        # anonymous link
        if len(self.inline_markup_stack) is 1:
            content += ('<%s>`__' % self.inline_markup_stack[0])
        else:
            content += ' '.join(self.inline_markup_stack[1:None])
            content += (' <%s>`_' % self.inline_markup_stack[0])

        self.content.append(content)
        self.inline_markup_stack[:] = []
        self.no_space = False
        self.hyperlink_end = True


class WADLHandler(xml.sax.ContentHandler):

    def __init__(self, filename, api_ref):
        self.filename = filename
        self.api_ref = api_ref
        self.method_tag_map = {method.split('#', 1)[1]: tag
                               for method, tag
                               in self.api_ref['method_tags'].items()
                               if method.split('#', 1)[0] == filename}
        self.resource_tag_map = {resource.split('#', 1)[1]: tag
                                 for resource, tag
                                 in self.api_ref['resource_tags'].items()
                                 if resource.split('#', 1)[0] == filename}
        self.file_tag = self.api_ref['file_tags'].get(filename, None)
        self.actual_tags = set(tag['name'] for tag in self.api_ref['tags'])

    def startDocument(self):
        # API state
        self.apis = {}
        self.current_api = None
        self.schemas = {}

        # Resource Mapping
        self.resource_map = {}
        self.resource_types = {}
        self.resource_ids = defaultdict(list)
        self.resource_id_stack = []

        # URL paths
        self.url_map = {}
        self.url_params = {}
        self.url = []

        # general state
        self.tag_stack = []
        self.attr_stack = []
        self.content = None
        self.parser = None

    def detach_subparser(self, result, **kwargs):
        self.parser = None
        self.result_fn(result, **kwargs)
        self.result_fn = None

    def attach_subparser(self, parser, result_fn):
        self.parser = parser
        self.result_fn = result_fn

    def endDocument(self):
        for api in self.apis.values():
            for method in api:
                method['consumes'] = list(method['consumes'])
                method['produces'] = list(method['produces'])

    def parameter_description(self, content, **kwargs):
        name = self.search_stack_for('param')['name']
        self.url_params[name] = content.strip()

    def api_summary(self, content, **kwargs):
        if kwargs.get('shortdesc'):
            self.current_api['summary'] = kwargs['shortdesc']
        self.current_api['description'] = content.strip()

    def request_parameter_description(self, content, **kwargs):
        param = self.search_stack_for('param')
        style = STYLE_MAP[param['style']]
        name = param['name']
        if style == 'body':
            parameters = self.current_api['parameters']
            schema_name = parameters[0]['schema']['$ref'].rsplit('/', 1)[1]
            schema = self.schemas[schema_name]
            schema['properties'][name]['description'] = content.strip()
        else:
            self.current_api['parameters'][-1]['description'] = content.strip()

    def response_schema_description(self, content, **kwargs):
        status_code = self.search_stack_for('response')['status']
        if ' ' in status_code:
            status_codes = status_code.split(' ')
            if '200' in status_codes:
                status_code = '200'
            # TODO(arrsim) need to do something with the other status
            # codes
        param = self.search_stack_for('param')
        style = STYLE_MAP[param['style']]
        name = param['name']
        if style == 'header':
            response = self.current_api['responses'][status_code]
            response['headers'][name]['description'] = content.strip()
        elif style == 'body':
            parameters = self.current_api['parameters']
            schema_name = parameters[0]['schema']['$ref'].rsplit('/', 1)[1]
            schema_name = schema_name + '_' + status_code
            schema = self.schemas[schema_name]
            schema['properties'][name]['description'] = content.strip()

    def search_stack_for(self, tag_name):
        for tag, attrs in zip(reversed(self.tag_stack),
                              reversed(self.attr_stack)):
            if tag == tag_name:
                return attrs

    def on_top_tag_stack(self, *args):
        return self.tag_stack[-len(args):] == list(args)

    def startElement(self, name, _attrs):
        attrs = dict(_attrs)
        if name == 'wadl:doc':
            if self.on_top_tag_stack('resource', 'param'):
                self.attach_subparser(ParaParser(self),
                                      self.parameter_description)
            if self.on_top_tag_stack('method'):
                self.current_api['title'] = attrs.get('title')
                self.attach_subparser(ParaParser(self), self.api_summary)

            if self.on_top_tag_stack('request', 'representation',
                                     'param'):
                self.attach_subparser(ParaParser(self),
                                      self.request_parameter_description)
            if self.on_top_tag_stack('response', 'representation', 'param'):
                self.attach_subparser(ParaParser(self),
                                      self.response_schema_description)

        if self.parser:
            return self.parser.startElement(name, _attrs)

        self.tag_stack.append(name)
        self.attr_stack.append(attrs)
        self.content = []
        if name == 'method':
            if 'id' in attrs and 'name' in attrs:
                id = attrs['id']
                if id in self.url_map:
                    url = self.url_map[id]
                elif id in self.resource_map:
                    resource = self.resource_map[id]
                    url = self.resource_types[resource]
                else:
                    log.warning("Can't find method %s", id)
                    # Create the minimal object to prevent creating
                    # exceptions for this case everywhere.
                    self.current_api = {
                        'produces': set(),
                        'consumes': set(),
                        'examples': {},
                        'responses': {},
                        'parameters': {},
                    }
                    return
                tag = self.method_tag_map.get(id, '')
                name = attrs['name'].lower()
                if url in self.apis:
                    root_api = self.apis[url]
                else:
                    self.apis[url] = root_api = []
                self.current_api = {
                    'id': id,
                    'tags': set(),
                    'method': name,
                    'produces': set(),
                    'consumes': set(),
                    'examples': {},
                    'parameters': [{'in': "body",
                                    'name': "body",
                                    'description': "",
                                    'required': False,
                                    'schema': {
                                        '$ref': "#/definitions/%s" % id
                                    }}],
                    'responses': {},
                }
                if tag:
                    self.current_api['tags'].add(tag)
                elif id in self.resource_ids:
                    for tag_id in reversed(self.resource_ids[id]):
                        r_tag_id = self.resource_tag_map.get(tag_id)
                        if r_tag_id not in self.actual_tags:
                            continue
                        self.current_api['tags'].add(r_tag_id)
                        break
                if not self.current_api['tags']:
                    if self.file_tag:
                        self.current_api['tags'].add(self.file_tag)
                self.current_api['tags'] = list(self.current_api['tags'])
                # If there are no tags then we couldn't find the
                # method in the chapters.
                if self.current_api['tags']:
                    root_api.append(self.current_api)
                else:
                    log.warning("No tags for method %s" % id)

                for param, doc in self.url_params.items():
                    if ('{%s}' % param) in url:
                        self.current_api['parameters'].append(
                            create_parameter(param, 'template', doc))

        # URL paths
        if name == 'resource':
            self.url.append(attrs.get('path', '').replace('//', '/'))
            self.resource_id_stack.append(attrs.get('id', None))
        if self.on_top_tag_stack('resource_type', 'method'):
            self.resource_map[attrs.get('href').strip('#')] \
                = self.attr_stack[-2]['id']

        # Methods and Resource Types
        if name == 'resource' and attrs.get('type'):
            self.resource_types[attrs.get('type').strip('#')] \
                = join_url(self.url)
        if self.on_top_tag_stack('resource', 'method'):
            href = attrs.get('href').strip('#')
            self.url_map[href] = join_url(self.url)
            self.resource_ids[href] = [r_id for r_id in self.resource_id_stack
                                       if r_id]

        if name == 'xsdxt:code':
            if not attrs.get('href'):
                return
            if self.search_stack_for('response') is not None:
                type = 'response'
                status_code = self.search_stack_for('response')['status']
                if ' ' in status_code:
                    status_codes = status_code.split(' ')
                    if '200' in status_codes:
                        status_code = '200'
                    # TODO(arrsim) need to do something with the other
                    # status codes
            elif self.search_stack_for('request') is not None:
                type = 'request'
            else:
                log.error("Can't find request or response tag. %s",
                          self.tag_stack)
                raise Exception("Can't find request or response tag.")
            media_type = MIME_MAP[attrs['href'].rsplit('.', 1)[-1]]

            # XML is removed, skip all these
            if media_type == 'application/xml':
                return

            pathname = path.join(path.dirname(self.filename), attrs['href'])
            try:
                sample = open(pathname).read()
                if media_type == 'application/json':
                    sample = json.loads(sample)
            except IOError:
                log.warning("Can't find file %s" % pathname)
                sample = None

            if media_type != 'text/plain':
                self.current_api['produces'].add(media_type)
                self.current_api['consumes'].add(media_type)
            if sample and type == 'response':
                response = self.current_api['responses'][status_code]
                response['examples'][media_type] = sample
            elif sample and type == 'request':
                # Add request examples (Not swagger supported)
                self.current_api['examples'][media_type] = sample

        if name == 'response':
            if 'status' not in attrs:
                return
            status_code = attrs['status']
            response = {
                'headers': {},
                'examples': {},
            }
            if ' ' in status_code:
                status_codes = status_code.split(' ')
                for status_code in status_codes:
                    # For each of the multiple status make copies of
                    # blank responses?  The duplicates will be ignored
                    # by subsequent calls that update the response object.
                    self.current_api['responses'][status_code] = copy(response)
            else:
                self.current_api['responses'][status_code] = response

        if self.on_top_tag_stack('request', 'representation', 'param'):
            parameters = self.current_api['parameters']
            name = attrs['name']
            parameter = create_parameter(
                name=name,
                _in=attrs.get('style', 'plain'),
                description='',
                type=attrs.get('type', 'string'),
                required=attrs.get('required'))
            if parameter['in'] == 'body':
                schema_name = parameters[0]['schema']['$ref'].rsplit('/', 1)[1]
                if schema_name not in self.schemas:
                    self.schemas[schema_name] = {'type': 'object',
                                                 'properties': {}}
                schema_properties = self.schemas[schema_name]['properties']
                schema_properties[parameter['name']] = parameter
                del parameter['name']
                del parameter['in']
            else:
                parameters.append(parameter)
        if self.on_top_tag_stack('response', 'representation', 'param'):
            parameters = self.current_api['parameters']
            status_code = self.attr_stack[-3]['status']
            if ' ' in status_code:
                status_codes = status_code.split(' ')
                if '200' in status_codes:
                    status_code = '200'
                # TODO(arrsim) need to do something with the other status codes
            name = attrs['name']
            parameter = create_parameter(
                name=name,
                _in=attrs.get('style', 'plain'),
                description='',
                type=attrs.get('type', 'string'),
                required=attrs.get('required'))
            if parameter['in'] == 'body':
                schema_name = parameters[0]['schema']['$ref'].rsplit('/', 1)[1]
                schema_name = schema_name + '_' + status_code
                if schema_name not in self.schemas:
                    self.schemas[schema_name] = {'type': 'object',
                                                 'properties': {}}
                schema_properties = self.schemas[schema_name]['properties']
                schema_properties[parameter['name']] = parameter
                del parameter['name']
                del parameter['in']
            elif parameter['in'] == 'header':
                headers = self.current_api['responses'][status_code]['headers']
                headers[parameter['name']] = parameter
                del parameter['name']
                del parameter['in']

    def endElement(self, name):
        if self.parser:
            return self.parser.endElement(name)

        if self.current_api and name == 'method':
            # Clean up the parameters of methods that have take no
            # body content.
            parameters = self.current_api['parameters']
            if parameters and 'schema' in parameters[0]:
                schema_name = parameters[0]['schema']['$ref'].rsplit('/', 1)[1]
                if schema_name not in self.schemas:
                    self.current_api['parameters'] \
                        = self.current_api['parameters'][1:]
        # URL paths
        if name == 'resource':
            self.url.pop()
            self.resource_id_stack.pop()

        self.tag_stack.pop()
        self.attr_stack.pop()

    def characters(self, content):
        if self.parser:
            return self.parser.characters(content)

        content = content.strip()
        if content:
            self.content.append(content)


def main1(source_file, output_dir):
    log.info('Reading API description from %s' % source_file)
    api_ref = json.load(open(source_file))
    files = set()
    for filepath in api_ref['method_tags'].keys():
        files.add(filepath.split('#', 1)[0])
    for filepath in api_ref['resource_tags'].keys():
        files.add(filepath.split('#', 1)[0])
    for filepath in api_ref['file_tags'].keys():
        files.add(filepath.split('#', 1)[0])

    # Load supplementary examples file
    examples_file = path.join(path.dirname(source_file),
                              api_ref['service'] + '-examples.json')
    if path.exists(examples_file):
        log.info('Reading examples from %s' % examples_file)
        examples = json.load(open(examples_file))
    else:
        examples = []

    output = {
        u'info': {
            'version': api_ref['version'],
            'title': api_ref['title'],
            'service': api_ref['service'],
            'license': {
                "name": "Apache 2.0",
                "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
            }
        },
        u'paths': defaultdict(list),
        u'schemes': {},
        u'tags': api_ref['tags'],
        u'basePath': {},
        u'securityDefinitions': {},
        u'host': {},
        u'definitions': {},
        u'externalDocs': {},
        u"swagger": u"2.0",
    }
    for file in files:
        log.info('Parsing %s' % file)
        abs_filename = path.abspath(file)
        ch = WADLHandler(abs_filename, api_ref)
        xml.sax.parse(file, ch)
        for urlpath, apis in ch.apis.items():
            output['paths'][urlpath].extend(apis)
        output['definitions'].update(ch.schemas)

    for ex_request, ex_response in examples:
        for urlpath in output['paths']:
            url_matcher = "^" + URL_TEMPLATE_RE.sub('[^/]+', urlpath) + "$"
            method = ex_request['method'].lower()
            if re.match(url_matcher, ex_request['url']):
                if len(output['paths'][urlpath]) > 1:
                    # Skip any of the multi-payload endpoints.  They
                    # are madness.
                    break

                for op in output['paths'][urlpath]:
                    operation = output['paths'][urlpath][0]
                    if operation['method'].lower() == method:
                        break
                else:
                    log.warning("Couldn't find any operations %s for %s",
                                method, urlpath)
                    break

                request = HTTP_REQUEST_TMPL.render(
                    headers=ex_request['headers'],
                    method=ex_request['method'],
                    url=ex_request['url'])
                operation['examples'] = {'text/plain': request}

                # Override any responses
                status_code = ex_response['status_code']
                response = HTTP_RESPONSE_TMPL.render(
                    status_code=status_code,
                    headers=ex_response['headers'],
                    body=ex_response['body'] or '')
                if status_code in operation['responses']:
                    operation['responses'][status_code]['examples'] = \
                        {'text/plain': response}
                else:
                    operation['responses'][status_code] = \
                        {'examples': {'text/plain': response}}
        else:
            log.warning("Service %s %s doesn't have matching "
                        "URL for example %s %s",
                        output['info']['service'], output['info']['version'],
                        method, ex_request['url'])

    os.chdir(output_dir)
    pathname = '%s-%s-swagger.json' % (api_ref['service'],
                                       api_ref['version'])
    with open(pathname, 'w') as out_file:
        json.dump(output, out_file, indent=2, sort_keys=True)


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
