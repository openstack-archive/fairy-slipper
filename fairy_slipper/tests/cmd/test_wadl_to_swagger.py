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

from fairy_slipper.cmd import wadl_to_swagger


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
        ch = wadl_to_swagger.ParaParser(parent)
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
        ch = wadl_to_swagger.ParaParser(parent)
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
        ch = wadl_to_swagger.ParaParser(parent)
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
        ch = wadl_to_swagger.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            "To create a keypair, see\n"
            "`<http://developer.openstack.org/#createKeypair>`__"
            " this link.\n\n")

    def test_para_inline_code(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>Code sample: <code>admin</code></para>
  <para><code>bget task</code>the program now!</para>
  <para>Code sample: <code>admin</code>more code on its way!</para>
  <para>Code sample:<code>admin</code>.</para>
  <para>para5</para>
</wadl:doc>
"""

        parent = MockParent()
        ch = wadl_to_swagger.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """Code sample: ``admin``

``bget task`` the program now!

Code sample: ``admin`` more code on its way!

Code sample: ``admin`` .

para5

""")

    def test_para_emphasis(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <para>Some text with <emphasis>bold words at the end of the sentence</emphasis>.</para>
  <para><emphasis>Bold text is cool</emphasis></para>
  <para>Multi word text is <emphasis>brilliant</emphasis>and then some.</para>
  <para>Lovely <emphasis>bold</emphasis></para>
  <para>para5</para>
</wadl:doc>
"""  # noqa

        parent = MockParent()
        ch = wadl_to_swagger.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """Some text with **bold words at the end of the sentence** .

**Bold text is cool**

Multi word text is **brilliant** and then some.

Lovely **bold**

para5

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
       ch = wadl_to_swagger.ParaParser(parent)
       xml.sax.parse(StringIO(file_content), ch)
       self.assertEqual(
           parent.result,
           """This operation does not accept a request body.\n\nExample requests and responses:\n\n- Show account details and list containers:\n\n  Some more details.\n\n- See the example response below.\n\n"""
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
        ch = wadl_to_swagger.ParaParser(parent)
        xml.sax.parse(StringIO(file_content), ch)
        self.assertEqual(
            parent.result,
            """This operation does not accept a request body.\n\nExample requests and responses:\n\n- Show account details and list containers:\n\n  ``curl -i $publicURL?format=json -X GET -H \"X-Auth-Token:\n  $token\"``\n\n  See the example response below.\n\n"""
        )


    def test_listitem_para_programlisting(self):
       file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
    <para>Delete the <code>steven</code>container:</para>
<itemizedlist>
<listitem>
<para>Container command:</para>
<para><code>curl -i $publicURL/steven -X DELETE -H "X-Auth-Token: $token"</code></para>
            <para>If the container does not exist, the response is:</para>
            <para><programlisting>HTTP/1.1 404 Not Found
Content-Length: 70
Content-Type: text/html; charset=UTF-8
Date: Thu, 16 Jan 2014 18:00:20 GMT
&lt;html>&lt;h1>Conflict&lt;/h1>&lt;p>Trying to complete your request.&lt;/p>&lt;/html>
</programlisting></para>
</listitem>
<listitem><para>Second container command:</para><para>Write to disk.</para>
</listitem>
</itemizedlist>
</wadl:doc>
"""

       parent = MockParent()
       ch = wadl_to_swagger.ParaParser(parent)
       xml.sax.parse(StringIO(file_content), ch)
       self.assertEqual(
           parent.result,
           """Delete the ``steven`` container:\n\n- Container command:\n\n  ``curl -i $publicURL/steven -X DELETE -H \"X-Auth-Token: $token\"``\n\n  If the container does not exist, the response is:\n\n  ::\n\n     HTTP/1.1 404 Not Found\n     Content-Length: 70\n     Content-Type: text/html; charset=UTF-8\n     Date: Thu, 16 Jan 2014 18:00:20 GMT\n     <html>\n     <h1>Conflict\n     </h1>\n     <p>Trying to complete your request.\n     </p>\n     </html>\n\n\n- Second container command:\n\n  Write to disk.\n\n"""
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
        ch = wadl_to_swagger.ParaParser(parent)
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
        ch = wadl_to_swagger.ParaParser(parent)
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
       ch = wadl_to_swagger.ParaParser(parent)
       xml.sax.parse(StringIO(file_content), ch)
       self.assertEqual(
           parent.result,
           """Example requests and responses:\n\n- Copy the ``goodbye`` object from the ``marktwain`` container to\n  the ``janeausten`` container: ``curl -i\n  $publicURL/marktwain/goodbye -X COPY -H "X-Auth-Token: $token" -H\n  "Destination: janeausten/goodbye"``  ::\n\n     HTTP/1.1 201 Created\n     Content-Length: 0\n     X-Copied-From: marktwain/goodbye\n\n\n"""
       )

    def test_table_caption(self):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>
<wadl:doc>
  <table><caption>Image status</caption></table>
  <table><caption>Image <code>with a code literal</code> <code>inside</code></caption></table>
  <table><caption>A <emphasis>bold</emphasis> caption <emphasis>again</emphasis></caption></table>
  <table><caption><emphasis role="italic">An italicized</emphasis> caption</caption></table>
  <table><caption>A caption with <emphasis>bold</emphasis> text embedded</caption></table>
</wadl:doc>
"""

        parent = MockParent()
        ch = wadl_to_swagger.ParaParser(parent)
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
      </representation>
    </response>
  </method>
</application>
        """

        ch = wadl_to_swagger.WADLHandler(filename, api_ref)
        xml.sax.parse(StringIO(file_content), ch)

        self.assertEqual(
            ch.apis,
            {'v2/':
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
                    'schema': {'$ref':
                               '#/definitions/createThing'}}],
               'produces': [],
               'responses': {'202': {'examples': {},
                                     'headers': {}}},
               'summary': 'Creates and uses a port interface '
               'to attach the port to a server instance.',
               'tags': ['things'],
               'title': 'Create interface'}]})

        self.assertEqual(
            ch.schemas,
            {'createThing':
             {'properties':
              {'thing-a-imagig':
               {'description':
                'Specify the ``interfaceAttachment``'
                ' action in the request body.',
                'format': '',
                'required': True,
                'type': 'string'}},
              'type': 'object'}})
