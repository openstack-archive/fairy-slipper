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
import unittest
import xml.sax

from fairy_slipper.cmd import wadl_to_swagger_valid


class MockParent(object):
    result = None
    rest = None

    def detach_subparser(self, result, **kwargs):
        self.result = result
        self.kwargs = kwargs


class TestParaParser(unittest.TestCase):

    def test_code_block(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>This is an example request:</para>
  <programlisting>GET /v2.0/routers/{router_id}
Accept: application/json</programlisting>
  <para>para2</para>
</wadl:doc>
"""

        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """This is an example request:

::

   GET /v2.0/routers/{router_id}
   Accept: application/json

para2

""")

    def test_code_block_language(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>This is an example request:</para>
<programlisting language="json">"OS-OAUTH1": {
    "access_token_id": "cce0b8be7"
}</programlisting>
  <para>para2</para>
</wadl:doc>
"""

        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """This is an example request:

.. code-block:: json

   "OS-OAUTH1": {
       "access_token_id": "cce0b8be7"
   }

para2

""")

    def test_link(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>
    To create a keypair, make a <link
    xlink:href="http://developer.openstack.org/#createKeypair">
    create keypair</link> request.
  </para>
</wadl:doc>
"""

        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            "To create a keypair, make a "
            "`create keypair\n"
            "<http://developer.openstack.org/#createKeypair>`_"
            " request.\n\n")

    def test_anonymous_link(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>
    To create a keypair, see <link
    xlink:href="http://developer.openstack.org/#createKeypair"></link> this link.
  </para>
</wadl:doc>
"""  # noqa

        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            "To create a keypair, see\n"
            "`<http://developer.openstack.org/#createKeypair>`__"
            " this link.\n\n")

    def test_para_inline_code(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>Code sample <code>admin</code></para>
  <para><code>get task</code>, program!</para>
  <para><code>get task</code> program!</para>
  <para>Code sample <code>admin</code> and more code.</para>
  <para>Code <code>admin</code>.</para>
  <para>Code <code>admin</code>. Another sentence started.</para>
  <para>para5</para>
  <para>Code <code>test</code>: with colon</para>
  <para>Code <code>test</code>; with semi-colon</para>
  <para>Code <code>test</code>; with semi-colon and <code>
  end test</code>.</para>
  <para>Code (<code>test</code>) with parens.</para>
</wadl:doc>
"""

        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """Code sample ``admin``

``get task``, program!

``get task`` program!

Code sample ``admin`` and more code.

Code ``admin``.

Code ``admin``. Another sentence started.

para5

Code ``test``: with colon

Code ``test``; with semi-colon

Code ``test``; with semi-colon and ``end test``.

Code (``test``) with parens.

""")

    def test_para_emphasis(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>Some text with <emphasis>bold words at the end of the sentence</emphasis>.</para>
  <para><emphasis>Bold text is cool</emphasis></para>
  <para>Multi word text is <emphasis>brilliant</emphasis>and then some.</para>
  <para>Really <emphasis>bold</emphasis></para>
  <para>para5</para>
  <para>This is a <emphasis>sentence</emphasis>; another phrase follows.</para>
  <para>Text with (<emphasis>parenthesis</emphasis>) and then **text**: with colon.</para>
  <para>A <emphasis>comma</emphasis>, and more <code>text</code>.</para>
  <para>Some text with <emphasis>back</emphasis> <emphasis>to back</emphasis>
        emphasized text.</para>
</wadl:doc>
"""  # noqa

        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """Some text with **bold words at the end of the sentence**.

**Bold text is cool**

Multi word text is **brilliant** and then some.

Really **bold**

para5

This is a **sentence**; another phrase follows.

Text with (**parenthesis**) and then **text**: with colon.

A **comma**, and more ``text``.

Some text with **back** **to back** emphasized text.

""")

    def test_listitem_para(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>This operation does not accept a request body.</para>
  <para>Example requests and responses:</para>
  <itemizedlist>
     <listitem><para>Show account details and list containers:</para>
     <para>Some more details.</para>
     </listitem>
     <listitem><para>See the example response below.</para></listitem>
  </itemizedlist>
</wadl:doc>
"""
        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """This operation does not accept a request body.
\nExample requests and responses:
\n- Show account details and list containers:
\n  Some more details.
\n- See the example response below.\n\n"""
        )

    def test_nested_listitem(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
<itemizedlist>
<listitem>
<para>Para 1, listitem1</para>
<para>Para 2, listitem1</para>
<itemizedlist>
<listitem>
<para>Embedded item1</para>
</listitem>
<listitem>
<para>Embedded item2</para>
</listitem>
<listitem>
<para>Embedded item3</para>
</listitem>
</itemizedlist>
<para>Para 3, listitem1</para>
</listitem>
<listitem><para>Para1, listitem2</para></listitem>
</itemizedlist>
<para>Another para of text</para>
</wadl:doc>
"""
        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """- Para 1, listitem1\n\n  Para 2, listitem1\n\n  - Embedded item1
\n  - Embedded item2\n\n  - Embedded item3\n\n  Para 3, listitem1
\n- Para1, listitem2\n\nAnother para of text\n\n"""
        )

    def test_listitem_para_code(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
   <para>This operation does not accept a request body.</para>
   <para>Example requests and responses:</para>
   <itemizedlist>
      <listitem><para>Show account details and list containers:</para>
                <para><code>curl -i
                            $publicURL?format=json -X GET -H
                            "X-Auth-Token: $token"</code></para>
                <para>See the example response below.</para>
      </listitem>
      </itemizedlist>
</wadl:doc>
"""
        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """This operation does not accept a request body.
\nExample requests and responses:
\n- Show account details and list containers:
\n  ``curl -i $publicURL?format=json -X GET -H \"X-Auth-Token:\n  $token\"``
\n  See the example response below.\n\n"""
        )

    def test_listitem_para_programlisting(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
<para>Delete the <code>steven</code>container:</para>
<itemizedlist>
<listitem>
<para>Container command:</para>
<para>
<code>curl -i $publicURL/steven
 -X DELETE -H "X-Auth-Token: $token"</code>
</para>
<para>If the container does not exist, the response is:</para>
<para><programlisting>HTTP/1.1 404 Not Found
Content-Length: 70
Content-Type: text/html; charset=UTF-8
Date: Thu, 16 Jan 2014 18:00:20 GMT
&lt;html>
&lt;h1>Conflict&lt;/h1>
&lt;p>Trying to complete your request.&lt;/p>&lt;/html>
</programlisting></para>
</listitem>
<listitem><para>Second container command:</para><para>Write to disk.</para>
</listitem>
</itemizedlist>
</wadl:doc>
"""
        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """Delete the ``steven`` container:
\n- Container command:
\n  ``curl -i $publicURL/steven -X DELETE -H \"X-Auth-Token: $token\"``
\n  If the container does not exist, the response is:
\n  ::\n\n     HTTP/1.1 404 Not Found\n     Content-Length: 70
     Content-Type: text/html; charset=UTF-8
     Date: Thu, 16 Jan 2014 18:00:20 GMT
     <html>\n     <h1>Conflict\n     </h1>
     <p>Trying to complete your request.\n     </p>
     </html>\n\n\n- Second container command:
\n  Write to disk.\n\n"""
        )

    def test_para_code_block(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>This is an example request:</para>
  <para><programlisting>GET /v2.0/routers/{router_id}
Accept: application/json</programlisting></para>
  <para>para2</para>
</wadl:doc>
"""
        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """This is an example request:

::

   GET /v2.0/routers/{router_id}
   Accept: application/json


para2

""")

    def test_para_code_block_language(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>This is an example request:</para>
<para><programlisting language="json">"OS-OAUTH1": {
    "access_token_id": "cce0b8be7"
}</programlisting></para>
  <para>para2</para>
</wadl:doc>
"""
        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """This is an example request:

.. code-block:: json

   "OS-OAUTH1": {
       "access_token_id": "cce0b8be7"
   }


para2

""")

    def test_listitem_all_in_one_para(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
        <para>Example requests and responses:</para>
            <itemizedlist>
                <listitem><para>Copy the <code>goodbye</code> object
                        from the <code>marktwain</code> container to
                        the <code>janeausten</code> container:
                            <code>curl -i $publicURL/marktwain/goodbye
                            -X COPY -H "X-Auth-Token: $token" -H
                            "Destination: janeausten/goodbye"</code>
                        <programlisting>HTTP/1.1 201 Created
Content-Length: 0
X-Copied-From: marktwain/goodbye
</programlisting></para></listitem>
</itemizedlist>
</wadl:doc>
"""
        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """Example requests and responses:
\n- Copy the ``goodbye`` object from the ``marktwain`` container to
  the ``janeausten`` container: ``curl -i
  $publicURL/marktwain/goodbye -X COPY -H "X-Auth-Token: $token" -H
  "Destination: janeausten/goodbye"``  ::\n\n     HTTP/1.1 201 Created
     Content-Length: 0\n     X-Copied-From: marktwain/goodbye\n\n\n"""
        )

    def test_table_caption(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <table><caption>Image status</caption></table>
  <table><caption>Image <code>with a code literal</code>
  <code>inside</code></caption></table>
  <table>
  <caption>A <emphasis>bold</emphasis> caption <emphasis>again</emphasis>
  </caption></table>
  <table>
  <caption>
  <emphasis role="italic">An italicized</emphasis> caption</caption>
  </table>
  <table>
  <caption>A caption with <emphasis>bold</emphasis> text embedded</caption>
  </table>
</wadl:doc>
"""
        parent = MockParent()
        ch = wadl_to_swagger_valid.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """**Image status**

++

**Image with a code literal inside**

++

**A bold caption again**

++

**An italicized caption**

++

**A caption with bold text embedded**

++

""")


class TestWADLHandler(unittest.TestCase):

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
    <resource id="version" type="#VersionDetails" path="/v2">
      <method href="#createThing" />
    </resource>
  </resources>
  <method name="POST" id="createThing">
    <wadl:doc title="Create interface">
      <para role="shortdesc">Create a port interface.</para>
    </wadl:doc>
    <request>
      <representation mediaType="application/json">
        <param name="thing-a-imagig" style="plain"
               type="xsd:string" required="true">
          <wadl:doc>
            <para>
               Specify the <code>interfaceAttachment</code>
               action in the request body.
            </para>
          </wadl:doc>
        </param>
      </representation>
    </request>
    <response status="202">
      <representation mediaType="application/json">
        <param name="thing-a-imagig-response" style="plain"
               type="xsd:string" required="true">
          <wadl:doc>
            <para>
               Specify the <code>interfaceAttachment</code>
               action in the request body.
            </para>
          </wadl:doc>
        </param>
      </representation>
    </response>
  </method>
</application>
        """

        ch = wadl_to_swagger_valid.WADLHandler(filename, api_ref)
        xml.sax.parse(StringIO(file_content), ch)

        self.assertEqual(
            ch.apis,
            {'/v2':
             [{'method': 'post',
              'consumes': [],
               'description': '',
               'tags': ['things'],
               'x-title': 'Create interface',
               'operationId': 'createThing',
               'parameters': [
                   {'description': '',
                    'in': 'body',
                    'name': 'body',
                    'required': False,
                    'schema': {'$ref':
                               '#/definitions/createThing'}}],
               'produces': [],
               'responses': {'202': {'examples': {},
                                     'headers': {},
                                     'schema': {
                                         '$ref':
                                         '#/definitions/createThing_202'},
                                     'description': ''}},
               'summary': 'Create a port interface.'}]})

        # api structure differs from final swagger file output
        self.assertEqual(
            ch.schemas,
            {'createThing':
             {'required': ['thing-a-imagig'],
              'properties':
              {'thing-a-imagig':
               {'description':
                'Specify the ``interfaceAttachment``'
                ' action in the request body.',
                'format': '',
                'type': 'string'}},
              'type': 'object'},
             'createThing_202':
             {'required': ['thing-a-imagig-response'],
              'properties':
              {'thing-a-imagig-response':
               {'description':
                'Specify the ``interfaceAttachment``'
                ' action in the request body.',
                'format': '',
                'type': 'string'}},
              'type': 'object'}}
        )

    def test_wadl_copy_method(self):
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
    <resource id="version" type="#VersionDetails" path="/v2">
      <method href="#copyThing" />
    </resource>
  </resources>
  <method name="COPY" id="copyThing">
    <wadl:doc title="Copy interface">
      <para role="shortdesc">Copy a port interface.</para>
    </wadl:doc>
    <request>
      <representation mediaType="application/json">
        <param name="copy-request" style="plain"
               type="xsd:string" required="true">
          <wadl:doc>
            <para>
               Copy the <code>interfaceAttachment</code>.
            </para>
          </wadl:doc>
        </param>
      </representation>
    </request>
    <response status="202">
      <representation mediaType="application/json">
        <param name="copy-response" style="plain"
               type="xsd:string" required="true">
          <wadl:doc>
            <para>
               Copy response text.
            </para>
          </wadl:doc>
        </param>
      </representation>
    </response>
  </method>
</application>
        """

        ch = wadl_to_swagger_valid.WADLHandler(filename, api_ref)
        xml.sax.parse(StringIO(file_content), ch)

        # api structure differs from final swagger file output
        self.assertEqual(
            ch.apis,
            {'/v2':
             [{'method': 'x-copy',
              'consumes': [],
               'description': '',
               'tags': ['things'],
               'x-title': 'Copy interface',
               'operationId': 'copyThing',
               'parameters': [
                   {
                       'description': '',
                       'in': 'body',
                       'name': 'body',
                       'required': False,
                       'schema': {'$ref': '#/definitions/copyThing'}
                   }],
               'produces': [],
               'responses': {'202': {'examples': {},
                                     'headers': {},
                                     'schema': {
                                         '$ref':
                                         '#/definitions/copyThing_202'},
                                     'description': ''}},
               'summary': 'Copy a port interface.'}]})

        self.assertEqual(
            ch.schemas,
            {'copyThing':
             {'required': ['copy-request'],
              'properties':
              {'copy-request':
               {'description':
                'Copy the ``interfaceAttachment``.',
                'format': '',
                'type': 'string'}},
              'type': 'object'},
             'copyThing_202':
             {'required': ['copy-response'],
              'properties':
              {'copy-response':
               {'description':
                'Copy response text.',
                'format': '',
                'type': 'string'}},
              'type': 'object'}}
        )

    def test_wadl_multiple_actions(self):
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
  <resources xml:id="os-server-actions-v2">
    <resource id="server_id" type="#VersionDetails" path="/v2">
      <method href="#doThing1" />
      <method href="#doThing2" />
    </resource>
  </resources>
  <method name="POST" id="doThing1">
    <wadl:doc title="Create interface">
      <para role="shortdesc">Create a port interface.</para>
    </wadl:doc>
    <request>
      <representation mediaType="application/json">
        <param name="copy-request" style="plain"
               type="xsd:string" required="true">
          <wadl:doc>
            <para>
               Copy the <code>interfaceAttachment</code>.
            </para>
          </wadl:doc>
        </param>
      </representation>
    </request>
    <response status="202">
      <representation mediaType="application/json">
        <param name="copy-response" style="plain"
               type="xsd:string" required="true">
          <wadl:doc>
            <para>
               Copy response text.
            </para>
          </wadl:doc>
        </param>
      </representation>
    </response>
  </method>
  <method name="POST" id="doThing2">
    <wadl:doc title="Create interface">
      <para role="shortdesc">Create a port interface.</para>
    </wadl:doc>
    <request>
      <representation mediaType="application/json">
        <param name="copy-request" style="plain"
               type="xsd:string" required="true">
          <wadl:doc>
            <para>
               Copy the <code>interfaceAttachment</code>.
            </para>
          </wadl:doc>
        </param>
      </representation>
    </request>
    <response status="202">
      <representation mediaType="application/json">
        <param name="copy-response" style="plain"
               type="xsd:string" required="true">
          <wadl:doc>
            <para>
               Copy response text.
            </para>
          </wadl:doc>
        </param>
      </representation>
    </response>
  </method>
</application>
        """

        ch = wadl_to_swagger_valid.WADLHandler(filename, api_ref)
        xml.sax.parse(StringIO(file_content), ch)

        # api structure differs from final swagger file output
        self.assertEqual(
            ch.apis,
            {'/v2':
             [{'method': 'post',
              'consumes': [],
               'description': '',
               'tags': ['things'],
               'x-title': 'Create interface',
               'operationId': 'doThing1',
               'parameters': [
                   {
                       'description': '',
                       'in': 'body',
                       'name': 'body',
                       'required': False,
                       'schema': {'$ref': '#/definitions/doThing1'}
                   }],
               'produces': [],
               'responses': {'202': {'examples': {},
                                     'headers': {},
                                     'schema': {
                                         '$ref':
                                         '#/definitions/doThing1_202'},
                                     'description': ''}},
               'summary': 'Create a port interface.'},
              {'method': 'post',
              'consumes': [],
               'description': '',
               'tags': ['things'],
               'x-title': 'Create interface',
               'operationId': 'doThing2',
               'parameters': [
                   {
                       'description': '',
                       'in': 'body',
                       'name': 'body',
                       'required': False,
                       'schema': {'$ref': '#/definitions/doThing2'}
                   }],
               'produces': [],
               'responses': {'202': {'examples': {},
                                     'headers': {},
                                     'schema': {
                                         '$ref':
                                         '#/definitions/doThing2_202'},
                                     'description': ''}},
               'summary': 'Create a port interface.'}]})

        self.assertEqual(
            ch.schemas,
            {'doThing1':
             {'required': ['copy-request'],
              'properties':
              {'copy-request':
               {'description':
                'Copy the ``interfaceAttachment``.',
                'format': '',
                'type': 'string'}},
              'type': 'object'},
             'doThing1_202':
             {'required': ['copy-response'],
              'properties':
              {'copy-response':
               {'description':
                'Copy response text.',
                'format': '',
                'type': 'string'}},
              'type': 'object'},
             'doThing2':
             {'required': ['copy-request'],
              'properties':
              {'copy-request':
               {'description':
                'Copy the ``interfaceAttachment``.',
                'format': '',
                'type': 'string'}},
              'type': 'object'},
             'doThing2_202':
             {'required': ['copy-response'],
              'properties':
              {'copy-response':
               {'description':
                'Copy response text.',
                'format': '',
                'type': 'string'}},
              'type': 'object'}}
        )
