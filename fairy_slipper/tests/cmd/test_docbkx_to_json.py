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

from __future__ import unicode_literals

import os
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from unittest import TestCase
import xml.sax

from fairy_slipper.cmd import docbkx_to_json


class TestChapterParaParser(TestCase):

    def test_para_inline_code(self):
        filename = "test-file.xml"
        test_filename = os.path.dirname(os.path.abspath(__file__))
        test_filename += "/ch_test-v1.xml"

        file_content = """<?xml version="1.0" encoding="UTF-8"?>
        <book xml:id="test-v1" version="1">
        <xi:include href="%s"/>
        </book>
        """ % (test_filename)

        ch = docbkx_to_json.APIRefContentHandler(filename)
        xml.sax.parse(StringIO(file_content), ch)

        self.assertEqual(
            ch.tags,
            [{
                'name': 'test-v1',
                'summary': "Image operations ``show`` all fields.\n"
                "\nCreates, lists, updates, and deletes images.\n"
                "\nCreates, **lists**, ``updates`` and **deletes images**"
                "\n\nCreates, (``x+5``), and deletes **images**."}]
        )

    def test_code_block(self):
        filename = "test-file.xml"
        test_filename = os.path.dirname(os.path.abspath(__file__))
        test_filename += "/ch_test-v3.xml"

        file_content = """<?xml version="1.0" encoding="UTF-8"?>
        <book xml:id="test-v3" version="3">
        <xi:include href="%s"/>
        </book>
        """ % (test_filename)

        ch = docbkx_to_json.APIRefContentHandler(filename)
        xml.sax.parse(StringIO(file_content), ch)

        self.assertEqual(
            ch.tags,
            [{
                'name': 'test-v3',
                'summary': "You can encode sets into a blob. Do something with ``type`` to\n``application/json`` and JSON strings in a ``blob``. Example:\n\n::\n\n   \"blob\": {\n           \"default\": false\n       }\n\nOr:\n\n::\n\n   \"blob\": {\n           \"foobar_user\": [\n               \"role:compute-user\"\n           ]\n       }"  # noqa
            }]
        )

    def test_table_caption(self):
        filename = "test-file.xml"
        test_filename = os.path.dirname(os.path.abspath(__file__))
        test_filename += "/ch_test-table.xml"

        file_content = """<?xml version="1.0" encoding="UTF-8"?>
        <book xml:id="table-v3" version="1">
        <xi:include href="%s"/>
        </book>
        """ % (test_filename)

        ch = docbkx_to_json.APIRefContentHandler(filename)
        xml.sax.parse(StringIO(file_content), ch)

        self.assertEqual(
            ch.tags,
            [{
                'name': 'table-v3',
                'summary': "Creates, lists, updates images.\n"
                "\n**Image status**\n\n++\n"
                "\n**Image with embedded bold status**\n\n++"
            }]
        )

    def test_nested_listitems(self):
        filename = "test-file.xml"
        test_filename = os.path.dirname(os.path.abspath(__file__))
        test_filename += "/ch_test-listitems.xml"

        file_content = """<?xml version="1.0" encoding="UTF-8"?>
        <book xml:id="listitems-v1" version="1">
        <xi:include href="%s"/>
        </book>
        """ % (test_filename)

        ch = docbkx_to_json.APIRefContentHandler(filename)
        xml.sax.parse(StringIO(file_content), ch)

        self.assertEqual(
            ch.tags,
            [{
                'name': 'listitems-v1',
                'summary': "- Para 1, listitem1\n\n  Para 2, listitem1\n\n"
                "  - Embedded item1\n\n  - Embedded item2\n"
                "\n  - Embedded item3\n\n"
                "  Para 3, listitem1\n\n- Para1, listitem2\n"
                "\nsome more para text"
            }]
        )

    def test_link(self):
        filename = "test-file.xml"
        test_filename = os.path.dirname(os.path.abspath(__file__))
        test_filename += "/ch_test-link.xml"

        file_content = """<?xml version="1.0" encoding="UTF-8"?>
        <book xml:id="link-v1" version="1">
        <xi:include href="%s"/>
        </book>
        """ % (test_filename)

        ch = docbkx_to_json.APIRefContentHandler(filename)
        xml.sax.parse(StringIO(file_content), ch)

        self.assertEqual(
            ch.tags,
            [{
                'name': 'link-v1',
                'summary': "To create a keypair, make a "
                "`create keypair"
                "\n<http://developer.openstack.org/#createKeypair>`_"
                " request.\n\n"
                "To test a link that ends the sentence, make a "
                "`create keypair\n"
                "<http://developer.openstack.org/#createKeypair>`_."
            }]
        )
