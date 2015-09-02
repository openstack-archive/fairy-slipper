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

from unittest import TestCase
from StringIO import StringIO
import xml.sax

from fairy_slipper.cmd import wadl_to_swagger


class TestWADLHandler(TestCase):

    def test_simple_wadl(self):
        filename = "api-v1.wadl"
        api_ref = {
            "file_tags": {filename: 'things'},
            "method_tags": {
            },
            "resource_tags": {
            },
            "service": "lorem",
            "tags": [],
            "title": "Lorem Ipsum",
            "version": "v1"
        }

        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<application>
  <resources xml:id="os-attach-v2">
    <resource id="version" type="#VersionDetails" path="v2/">
      <method href="#createThing" />
    </resource>
  </resources>
  <method name="POST" id="createThing">
    <wadl:doc title="Create interface">
      <para role="shortdesc">Creates and uses a port interface
        to attach the port to a server instance.</para>
    </wadl:doc>
    <request>
      <representation mediaType="application/json">
        <param name="thing-a-imagig" style="plain" type="xsd:string" required="true">
          <wadl:doc>
            <para>Specify the <code>interfaceAttachment</code> action in the request body.</para>
          </wadl:doc>
        </param>
      </representation>
    </request>
    <response status="202">
      <representation mediaType="application/json">
      </representation>
    </response>
  </method>
</application>
        """

        ch = wadl_to_swagger.WADLHandler(filename, api_ref)
        xml.sax.parse(StringIO(file_content), ch)

        assert ch.apis == {'v2/':
                           [{'consumes': [],
                             'description': '',
                             'examples': {},
                             'id': 'createThing',
                             'method': 'post',
                             'parameters': [
                                 {'description': '',
                                  'in': 'body',
                                  'name': 'body',
                                  'required': False,
                                  'schema': {'$ref': '#/definitions/createThing'}}],
                             'produces': [],
                             'responses': {'202': {'examples': {},
                                                   'headers': {}}},
                             'summary': 'Creates and uses a port interface '
                             'to attach the port to a server instance.',
                             'tags': ['things'],
                             'title': 'Create interface'}]}

        assert ch.schemas == {'createThing':
                              {'properties':
                               {'thing-a-imagig':
                                {'description':
                                 'Specify the ``interfaceAttachment``'
                                 ' action in the request body.',
                                 'format': '',
                                 'required': True,
                                 'type': 'string'}},
                               'type': 'object'}}
