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
import docutils.core
from docutils import nodes
import docutils.parsers.rst
import docutils.utils
from docutils import writers
import json
import logging
from os import path

logger = logging.getLogger(__name__)


class JSONTranslator(nodes.SparseNodeVisitor):
    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        self.output = {}
        self.node_stack = []
        self.node_stack.append(self.output)
        self.current_node_name = None
        self.bullet_stack = []
        self.table_stack = []
        self.text = ''
        self.col_num = 0
        self.first_row = 0
        self.hyperlink_name = ''
        self.refuri = ''
        self.listitem = False
        self.lit_block = False
        self.list_indent = 0
        self.text_res_desc = ''

    def visit_document(self, node):
        self.text = ''

    def depart_document(self, node):
        if self.text.endswith('\n\n'):
            self.text = self.text[:-2]
        self.output = self.text

    def default_visit(self, node):
        """Default node visit method."""
        self.current_node_name = node.__class__.__name__
        if hasattr(node, 'children') and node.children:
            new_node = {}
            self.node_stack[-1][self.current_node_name] = new_node
            self.node_stack.append(new_node)

    def default_departure(self, node):
        """Default node depart method."""
        if hasattr(node, 'children') and node.children:
            self.node_stack.pop()

    def visit_system_message(self, node):
        pass

    def depart_system_message(self, node):
        pass

    def visit_Text(self, node):
        if self.first_row is 0:
            if self.lit_block and len(self.bullet_stack) > 0:
                litblock = node.astext().split('\n')
                litblock = '\n        '.join(litblock)
                self.text += litblock
            else:
                self.text += node.astext()

    def depart_Text(self, node):
        pass

    def visit_emphasis(self, node):
        if self.first_row > 0:
            inlinetxt = self.table_stack.pop()
            para = inlinetxt.partition(node.astext())
            new_para = ''
            new_para += para[0] + '_' + para[1] + '_' + para[2]
            self.table_stack.append(new_para)
        else:
            self.text += '_'

    def depart_emphasis(self, node):
        if self.first_row is 0:
            self.text += '_'

    def visit_literal(self, node):
        if self.first_row > 0:
            inlinetxt = self.table_stack.pop()
            para = inlinetxt.partition(node.astext())
            new_para = ''
            new_para += para[0] + '`' + para[1] + '`' + para[2]
            self.table_stack.append(new_para)
        else:
            self.text += '`'

    def depart_literal(self, node):
        if self.first_row is 0:
            self.text += '`'

    def visit_strong(self, node):
        if self.first_row > 0:
            inlinetxt = self.table_stack.pop()
            para = inlinetxt.partition(node.astext())
            new_para = ''
            new_para += para[0] + '**' + para[1] + '**' + para[2]
            self.table_stack.append(new_para)
        else:
            self.text += '**'

    def depart_strong(self, node):
        if self.first_row is 0:
            self.text += '**'

    def visit_literal_block(self, node):
        if len(self.bullet_stack) > 0:
            self.text += '\n        '
        else:
            self.text += '```\n'
        self.lit_block = True

    def depart_literal_block(self, node):
        if len(self.bullet_stack) > 0:
            self.text += '\n'
        else:
            self.text += '\n```\n'
        self.lit_block = False

    def visit_bullet_list(self, node):
        if self.first_row > 0:
            self.text += """<ul>"""
        else:
            self.bullet_stack.append('*')

    def depart_bullet_list(self, node):
        if self.first_row > 0:
            self.text += """</ul>"""
        else:
            self.bullet_stack.pop()
            self.list_indent = len(self.bullet_stack) - 1
            if len(self.bullet_stack) is 0:
                self.text += '\n'

    def visit_list_item(self, node):
        if self.first_row > 0:
            self.text += """<li>"""
        else:
            self.list_indent = len(self.bullet_stack) - 1
            item = '\n%s%s ' % ('  ' * self.list_indent,
                                self.bullet_stack[-1])
            self.text += item
            self.listitem = True

    def depart_list_item(self, node):
        if self.first_row > 0:
            self.text += """</li>"""
        else:
            self.listitem = False
            self.list_indent = 0

    def visit_title(self, node):
        self.current_node_name = node.__class__.__name__
        if self.current_node_name not in self.node_stack[-1]:
            new_node = []
            self.node_stack[-1][self.current_node_name] = new_node
            self.node_stack.append(new_node)

    def depart_title(self, node):
        self.node_stack.pop()

    def visit_paragraph(self, node):
        if self.first_row > 0:
            self.table_stack.append(node.astext())
        else:
            # listitem text
            if self.listitem is True:
                pass
            else:
                # another para in listitem
                if len(self.bullet_stack) > 0:
                    if self.lit_block:
                        self.text += '\n' + '        '
                    else:
                        self.text += '\n' + '  ' * self.list_indent + ' '

    def depart_paragraph(self, node):
        if self.first_row is 0:
            if self.listitem:
                self.text += '\n'
                self.listitem = False
            else:
                if len(self.bullet_stack) > 0:
                    self.text += "\n"
                else:
                    # default paragraph
                    self.text += "\n\n"
        else:
            if self.first_row > 0:
                para = self.table_stack.pop()
                para = para.strip('\n')
                plist = para.split('\n')

                # multi-line text in single column
                if len(plist) > 0:
                    self.text += """<br>""".join(plist)
                else:
                    self.text += para

    def visit_line_block(self, node):
        if isinstance(self.node_stack[-1], list):
            return

        self.current_node_name = node.__class__.__name__
        if self.current_node_name not in self.node_stack[-1]:
            new_node = []
            self.node_stack[-1][self.current_node_name] = new_node
            self.node_stack.append(new_node)
        else:
            self.node_stack.append(self.node_stack[-1][self.current_node_name])

    def depart_line_block(self, node):
        if isinstance(self.node_stack[-1], list):
            self.node_stack.pop()

    def visit_table(self, node):
        self.col_num = 0

    def depart_table(self, node):
        self.text += "\n"

    def visit_tbody(self, node):
        pass

    def depart_tbody(self, node):
        self.text += "\n"
        self.first_row = 0
        self.col_num = 0

    def visit_thead(self, node):
        pass

    def depart_thead(self, node):
        pass

    def visit_tgroup(self, node):
        pass

    def depart_tgroup(self, node):
        pass

    def visit_colspec(self, node):
        pass

    def depart_colspec(self, node):
        pass

    def visit_row(self, node):
        if self.first_row is 1 and self.col_num > 0:
            row_separator = [' --- '] * self.col_num
            self.text += "|"
            sep_row = "|".join(row_separator)
            self.text += sep_row
            self.text += "|"
            self.text += "\n"

        self.text += "|"
        self.first_row += 1

    def depart_row(self, node):
        self.text += "\n"

    def visit_entry(self, node):
        self.text += " "

    def depart_entry(self, node):
        self.text += " |"
        self.col_num += 1

    def visit_definition(self, node):
        pass

    def depart_definition(self, node):
        pass

    def visit_definition_list(self, node):
        pass

    def depart_definition_list(self, node):
        pass

    def visit_definition_list_item(self, node):
        pass

    def depart_definition_list_item(self, node):
        pass

    def visit_term(self, node):
        self.text += "    "
        if self.first_row is 0:
            self.text += node.astext()
        else:
            self.table_stack.append(node.astext())

    def depart_term(self, node):
        if self.first_row > 0:
            self.text += self.table_stack.pop()
        self.text += """<br>"""

    def visit_reference(self, node):
        self.hyperlink_name = node.attributes['name']
        self.refuri = node.attributes['refuri']
        self.text += '['

    def depart_reference(self, node):
        if self.hyperlink_name:
            self.text += ']'
            self.text += '(' + self.refuri + ')'
        else:
            self.text += '[' + self.refuri + ']'

        self.hyperlink_name = ''
        self.refuri = ''


class JSONWriter(writers.Writer):

    supported = ('json',)
    """Formats this writer supports."""

    settings_spec = (
        '"Docutils JSON" Writer Options',
        None,
        [])

    config_section = 'docutils_json writer'
    config_section_dependencies = ('writers',)

    output = None

    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = JSONTranslator

    def set_doc(self, doc):
        self.document = doc

    def translate(self):
        self.visitor = visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.output


class error_writer(object):

    def write(self, line):
        logger.warning(line.strip())


def publish_string(string):
    optionP = docutils.frontend.OptionParser(
        components=(docutils.parsers.rst.Parser,))
    values = optionP.get_default_values()
    values.update({'output_encoding': 'unicode'}, optionP)
    document = docutils.utils.new_document(string, settings=values)
    parser.parse(string, document)
    settings_overrides = {'warning_stream': error_writer(),
                          'output_encoding': 'unicode'}
    json_writer = JSONWriter()
    json_writer.set_doc(document)

    return docutils.core.publish_string(
        string, writer=json_writer,
        settings_overrides=settings_overrides)


parser = docutils.parsers.rst.Parser()


def main1(filename, output_dir):
    logger.info('Loading %s' % filename)
    swagger = json.load(open(filename))
    write_md(swagger, output_dir)


def write_md(swagger, output_dir):
    info = swagger['info']
    version = info['version']
    service = info['x-service']
    output_file = '%s-%s-swagger-md.json' % (service, version)
    filepath = path.join(output_dir, output_file)
    logger.info('Output file: %s' % filepath)

    # convert tag x-summary
    for tag in swagger['tags']:
        new_desc = publish_string(tag['x-summary'])
        tag['x-summary'] = new_desc

    for paths, methods in swagger['paths'].items():
        for method, val in methods.items():
            # convert method description
            new_desc = publish_string(val['description'])
            val['description'] = new_desc

            # convert method summary
            if 'summary' in val:
                new_desc = publish_string(val['summary'])
                val['summary'] = new_desc

            # convert method x-title
            new_desc = publish_string(val['x-title'])
            val['x-title'] = new_desc

            # convert operation parameter descriptions
            for p in val['parameters']:
                new_desc = publish_string(p['description'])
                p['description'] = new_desc

            # convert response header descriptions
            for p, values in val['responses'].items():
                if 'headers' in values:
                    headers = values['headers']
                    for hkey, hval in headers.items():
                        new_desc = publish_string(hval['description'])
                        hval['description'] = new_desc

    # convert property descriptions in definitions
    for ops, vals in swagger['definitions'].items():
        for k, props in vals['properties'].items():
            new_desc = publish_string(props['description'])
            props['description'] = new_desc

    with codecs.open(filepath,
                     'w', "utf-8") as out_file:
        json.dump(swagger, out_file, indent=2, sort_keys=True)


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
