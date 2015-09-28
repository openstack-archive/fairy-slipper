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

import unittest

import docutils.core

from fairy_slipper import rest
from fairy_slipper.rest import JSONWriter


def minimal_method_json(consumes=[],
                        description='',
                        method='get',
                        parameters=[],
                        produces=[],
                        responses={},
                        summary='',
                        tags=[],
                        title=''):
    return dict(consumes=consumes,
                description=description,
                method=method,
                parameters=parameters,
                produces=produces,
                responses=responses,
                summary=summary,
                tags=tags,
                title=title)


class TestReSTMethod(unittest.TestCase):

    def test_no_path(self):
        rst = """
.. http:get::

"""
        json = rest.publish_string(rst)

        assert json == {'paths': {}, 'tags': []}

    def test_path_with_body(self):
        rst = """
.. http:get:: /path

   body

"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path': [
                            minimal_method_json(description='body\n\n')]},
                        'tags': []}

    def test_minimal(self):
        rst = """
.. http:%s:: /path

"""
        for method in ['get', 'post', 'put', 'patch',
                       'options', 'head', 'delete', 'copy']:
            json = docutils.core.publish_string(
                rst % method, writer=JSONWriter())

            assert json == {'paths':
                            {'/path': [
                                minimal_method_json(method=method)]},
                            'tags': []}

    def test_body_literal(self):
        rst = """
.. http:get:: /path

   literal block::

      banana
      1
      2
      3

"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description='''literal block:

```
banana
1
2
3
```
''')]},
                        'tags': []}

    def test_body_ul(self):
        rst = """
.. http:get:: /path

   Some normal body text

   - the first item
   - the second item

"""

        markdown = '''Some normal body text


 * the first item


 * the second item

'''
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_body_strong(self):
        rst = """
.. http:get:: /path

    start text **end**

    **start** end

    start **inline text** end

"""

        markdown = '''start text **end**

**start** end

start **inline text** end

'''
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_body_inline_literal(self):
        rst = """
.. http:get:: /path

    text ``end inline``

    ``start inline`` ending normal

    start text ``inline inline`` end text

"""

        markdown = '''text `end inline`

`start inline` ending normal

start text `inline inline` end text

'''
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_body_inline_emphasis(self):
        rst = """
.. http:get:: /path

    text *end inline*

    *start inline* ending normal

    start text *inline inline* end text

"""

        markdown = '''text _end inline_

_start inline_ ending normal

start text _inline inline_ end text

'''
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_synopsis(self):
        rst = """
.. http:get:: /path
   :synopsis: Some description of the operation
"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(
                             summary='Some description of the operation')]},
                        'tags': []}

    def test_title(self):
        rst = """
.. http:get:: /path
   :title: Path Thing
"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(title='Path Thing')]},
                        'tags': []}

    def test_hyperlink(self):
        rst = """
.. http:get:: /path

   For more information about form POST see `Object
   Storage API v1 (SUPPORTED) <http://docs.openstack.org/api
   /openstack-object-storage/1.0/content/>`_.

   Example requests and responses:

"""

        markdown = '''For more information about form POST see [Object\nStorage API v1 (SUPPORTED)](http://docs.openstack.org/api/openstack-object-storage/1.0/content/).

Example requests and responses:

'''  # noqa
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_table_simple(self):
        rst = """
.. http:get:: /path

   Some text before table


   +---------+---------+--------------+----------+
   | Field 1 | Field 2 | Field 3      | Field 4  |
   +---------+---------+--------------+----------+
   | Apply   | Name    | Description  | Required |
   +---------+---------+--------------+----------+

"""

        markdown = '''Some text before table

| Field 1 | Field 2 | Field 3 | Field 4 |
| --- | --- | --- | --- |
| Apply | Name | Description | Required |


'''

        json = rest.publish_string(rst)
        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_table_inline_strong(self):
        rst = """
.. http:get:: /path

   Some text before table


   +---------+---------------+-----------------+------------------+
   | Field 1 | Field 2       | Field 3         | Field 4          |
   +---------+---------------+-----------------+------------------+
   | Apply   | text in       |                 |                  |
   |         | **between**   |                 |                  |
   |         | text          | **text** start  | text **end**     |
   +---------+---------------+-----------------+------------------+

"""

        markdown = '''Some text before table

| Field 1 | Field 2 | Field 3 | Field 4 |
| --- | --- | --- | --- |
| Apply | text in<br>**between**<br>text | **text** start | text **end** |


'''

        json = rest.publish_string(rst)
        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_table_inline_emphasis(self):
        rst = """
.. http:get:: /path

   Some text before table


   +---------+---------------+-----------------+------------------+
   | Field 1 | Field 2       | Field 3         | Field 4          |
   +---------+---------------+-----------------+------------------+
   | Apply   | text in       |                 |                  |
   |         | *between*     |                 |                  |
   |         | text          | *text* start    | text *end*       |
   +---------+---------------+-----------------+------------------+

"""

        markdown = '''Some text before table

| Field 1 | Field 2 | Field 3 | Field 4 |
| --- | --- | --- | --- |
| Apply | text in<br>_between_<br>text | _text_ start | text _end_ |


'''
        json = rest.publish_string(rst)
        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_table_multiline_col_entry(self):

        rst = """
.. http:get:: /path

   Image status

   +----------------+---------------------------------------------------------------------+
   | Status         | Description                                                         |
   +----------------+---------------------------------------------------------------------+
   | queued         | The Image service reserved an image ID for the image in the         |
   |                | registry but has not uploaded any image data.                       |
   +----------------+---------------------------------------------------------------------+
   | saving         | The Image service is currently uploading the raw data for the       |
   |                | image.                                                              |
   +----------------+---------------------------------------------------------------------+

"""  # noqa
        markdown = '''Image status

| Status | Description |
| --- | --- |
| queued | The Image service reserved an image ID for the image in the<br>registry but has not uploaded any image data. |
| saving | The Image service is currently uploading the raw data for the<br>image. |


'''  # noqa

        json = rest.publish_string(rst)
        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_table_inline_literal(self):
        rst = """
.. http:get:: /path

   Some text before table


   +----------------+----------+--------------+----------------+
   | Field 1        | Field 2  | Field 3      | Field 4        |
   +----------------+----------+--------------+----------------+
   | End ``text``   | ``Name`` | Description  | ``start`` text |
   +----------------+----------+--------------+----------------+

"""

        markdown = '''Some text before table

| Field 1 | Field 2 | Field 3 | Field 4 |
| --- | --- | --- | --- |
| End `text` | `Name` | Description | `start` text |


'''

        json = rest.publish_string(rst)
        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(description=markdown)]},
                        'tags': []}

    def test_method_tags(self):
        rst = """
.. http:get:: /path

   :tag: cool-tag
   :tag: cool-tag1
"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(
                             tags=['cool-tag', 'cool-tag1'])]},
                        'tags': []}

    def test_produces(self):
        rst = """
.. http:get:: /path

   :produces: application/json
   :produces: text/plain
"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(
                             produces=['application/json',
                                       'text/plain'])]},
                        'tags': []}

    def test_accepts(self):
        rst = """
.. http:get:: /path

   :accepts: application/json
   :accepts: text/plain
"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(
                             consumes=['application/json',
                                       'text/plain'])]},
                        'tags': []}

    def test_parameter(self):
        rst = """
.. http:get:: /path

   :parameter thing: A parameter something.
"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(
                             parameters=[{
                                 'description': u'A parameter something.',
                                 'in': 'path',
                                 'name': u'thing',
                                 'required': True,
                                 'type': 'string'}])]},
                        'tags': []}

    def test_response_example(self):
        rst = """
.. http:get:: /path

   :responseexample 200: example.json
"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(
                             responses={'200':
                                        {'description': '',
                                         'examples':
                                         {'application/json':
                                          {'$ref':
                                           'example.json'}}}})]},
                        'tags': []}

    def test_statuscode(self):
        rst = """
.. http:get:: /path

   :statuscode 200: Success! Yeah!
"""
        json = rest.publish_string(rst)

        assert json == {'paths':
                        {'/path':
                         [minimal_method_json(
                             responses={'200':
                                        {'description': 'Success! Yeah!'}})]},
                        'tags': []}


class TestReSTTag(unittest.TestCase):

    def test_synopsis(self):
        rst = """
.. swagger:tag:: my-tag
   :synopsis: Interesting things!
"""
        json = rest.publish_string(rst)
        assert json == {'paths': {},
                        'tags': [{'name': 'my-tag',
                                  'description': '',
                                  'summary': 'Interesting things!'}]}

    def test_description(self):
        rst = """
.. swagger:tag:: my-tag

   body
"""
        json = rest.publish_string(rst)
        assert json == {'paths': {},
                        'tags': [{'name': 'my-tag',
                                  'description': 'body\n\n',
                                  'summary': ''}]}
