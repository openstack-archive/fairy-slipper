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

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from unittest import TestCase
import xml.sax
import os

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
                'summary': "Image operations ``show`` all fields.\n\nCreates, lists, updates, and deletes images."}]
        )
