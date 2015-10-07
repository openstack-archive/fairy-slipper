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

from fairy_slipper.cmd import tempest_log


SIMPLE_LOG = """2015-09-04 15:51:29.023 18793 DEBUG tempest_lib.common.rest_client [req-30784c0a-e9a1-4411-a7c1-20715b26598f ] Request (FlavorsV2TestJSON:setUpClass): 200 POST http://192.168.122.201:5000/v2.0/tokens
2015-09-04 15:51:29.023 18793 DEBUG tempest_lib.common.rest_client [req-30784c0a-e9a1-4411-a7c1-20715b26598f ] Request - Headers: {}
        Body: None
    Response - Headers: {'status': '200', 'content-length': '2987', 'vary': 'X-Auth-Token', 'server': 'Apache/2.4.7 (Ubuntu)', 'connection': 'close', 'date': 'Sun, 13 Sep 2015 07:43:01 GMT', 'content-type': 'application/json', 'x-openstack-request-id': 'req-1'}
        Body: None
2015-09-04 15:51:45.472 18793 INFO tempest_lib.common.rest_client [req-b710aeba-6263-4a49-bf50-2da42227c870 ] Request (FlavorsV2TestJSON:test_get_flavor): 200 POST http://192.168.122.201:5000/v2.0/tokens
2015-09-04 15:51:45.472 18793 DEBUG tempest_lib.common.rest_client [req-b710aeba-6263-4a49-bf50-2da42227c870 ] Request - Headers: {}
        Body: None
    Response - Headers: {'status': '200', 'content-length': '2987', 'vary': 'X-Auth-Token', 'server': 'Apache/2.4.7 (Ubuntu)', 'connection': 'close', 'date': 'Sun, 13 Sep 2015 07:43:01 GMT', 'content-type': 'application/json', 'x-openstack-request-id': 'req-2'}
        Body: None
"""  # noqa

SIMPLE_LOG_BODY = """2015-09-04 15:51:29.007 18793 INFO tempest_lib.common.rest_client [req-9e329507-e0ce-448c-a363-f49e39dd96b0 ] Request (FlavorsV2TestJSON:test_get_flavor): 200 GET http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1 0.117s
2015-09-04 15:51:29.007 18793 DEBUG tempest_lib.common.rest_client [req-9e329507-e0ce-448c-a363-f49e39dd96b0 ] Request - Headers: {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-Auth-Token': '<omitted>'}
        Body: None
    Response - Headers: {'status': '200', 'content-length': '430', 'content-location': 'http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1', 'x-compute-request-id': 'req-959a09e8-3628-419d-964a-1be4ca604232', 'vary': 'X-OpenStack-Nova-API-Version', 'connection': 'close', 'x-openstack-nova-api-version': '2.1', 'date': 'Sun, 13 Sep 2015 07:43:01 GMT', 'content-type': 'application/json'}
        Body: {"flavor": {"name": "m1.tiny", "links": [{"href": "http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1", "rel": "self"}, {"href": "http://192.168.122.201:8774/6b45254f6f7c44a1b65ddb8218932226/flavors/1", "rel": "bookmark"}], "ram": 512, "OS-FLV-DISABLED:disabled": false, "vcpus": 1, "swap": "", "os-flavor-access:is_public": true, "rxtx_factor": 1.0, "OS-FLV-EXT-DATA:ephemeral": 0, "disk": 1, "id": "1"}}
"""  # noqa

DEBUG_LOG = """2015-09-04 15:54:42.296 18793 INFO tempest_lib.common.rest_client [req-39c6042e-5a4a-4517-9fe9-32b34cfaa5a8 ] Request (TestSessionsTenantIsolation:test_delete_session_in_env_from_another_tenant): 403 DELETE http://127.0.0.1:8082/v1/environments/7501923609b145ec88eeb4a5c93e371c/sessions/db214e36e0494c4e9dc67fb0df8548f7 0.010s
2015-09-04 15:54:42.296 18793 DEBUG tempest_lib.common.rest_client [req-39c6042e-5a4a-4517-9fe9-32b34cfaa5a8 ] Request - Headers: {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-Auth-Token': '<omitted>'}
        Body: None
    Response - Headers: {'status': '403', 'content-length': '75', 'connection': 'close', 'date': 'Fri, 04 Sep 2015 15:54:42 GMT', 'content-type': 'text/plain; charset=UTF-8', 'x-openstack-request-id': 'req-39c6042e-5a4a-4517-9fe9-32b34cfaa5a8'}
        Body: 403 Forbidden

User is not authorized to access these tenant resources

    _log_request_full /opt/stack/new/tempest/.venv/local/lib/python2.7/site-packages/tempest_lib/common/rest_client.py:411
2015-09-04 15:52:13.727 18793 INFO tempest_lib.common.rest_client [req-0ff36a16-dacd-49c8-9835-7ce92d50f5a7 ] Request (TestEnvironmentsTenantIsolation:tearDown): 200 DELETE http://127.0.0.1:8082/v1/environments/c32c6d5095c4476da549ed065e9b5196 0.054s
2015-09-04 15:52:13.727 18793 DEBUG tempest_lib.common.rest_client [req-0ff36a16-dacd-49c8-9835-7ce92d50f5a7 ] Request - Headers: {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-Auth-Token': '<omitted>'}
        Body: None
    Response - Headers: {'status': '200', 'content-length': '0', 'connection': 'close', 'date': 'Fri, 04 Sep 2015 15:52:13 GMT', 'content-type': 'application/json', 'x-openstack-request-id': 'req-0ff36a16-dacd-49c8-9835-7ce92d50f5a7'}
        Body:  _log_request_full /opt/stack/new/tempest/.venv/local/lib/python2.7/site-packages/tempest_lib/common/rest_client.py:411
"""  # noqa


DEBUG_LOG_AUTH = """2015-09-04 15:49:46.056 14923 INFO tempest_lib.common.rest_client [req-280bc347-e650-473e-92bb-bcc59103e12c ] Request (main): 200 POST http://127.0.0.1:5000/v2.0/tokens
2015-09-04 15:49:46.056 14923 DEBUG tempest_lib.common.rest_client [req-280bc347-e650-473e-92bb-bcc59103e12c ] Request - Headers: {}
        Body: None
    Response - Headers: {'server': 'Apache/2.4.7 (Ubuntu)', 'vary': 'X-Auth-Token', 'x-openstack-request-id': 'req-280bc347-e650-473e-92bb-bcc59103e12c', 'content-length': '4846', 'connection': 'close', 'status': '200', 'content-type': 'application/json', 'date': 'Fri, 04 Sep 2015 15:49:42 GMT'}
        Body: None _log_request_full /opt/stack/new/tempest/.tox/venv/local/lib/python2.7/site-packages/tempest_lib/common/rest_client.py:411
"""  # noqa


def db_to_call_list(db):
    calls = []
    for req in sorted(db.requests):
        calls.append((db.requests[req], db.responses[req]))
    return calls


class TestLogParser(unittest.TestCase):
    maxDiff = 10000

    def test_simple_parse(self):
        result = db_to_call_list(
            tempest_log.parse_logfile(StringIO(SIMPLE_LOG)))
        self.assertEqual(result, [
            ({'url': '/v2.0/tokens',
              'service': 'identity',
              'headers': {},
              'body': None,
              'method': 'POST'},
             {'status_code': '200',
              'body': None,
              'headers': {'status': '200',
                          'content-length': '0',
                          'date': 'Sun, 13 Sep 2015 07:43:01 GMT',
                          'content-type': 'application/json',
                          'x-openstack-request-id': 'req-1',
                          'vary': 'X-Auth-Token',
                          'connection': 'close',
                          'server': 'Apache/2.4.7 (Ubuntu)'}}),
            ({'url': '/v2.0/tokens',
              'service': 'identity',
              'headers': {},
              'body': None,
              'method': 'POST'},
             {'status_code': '200',
              'body': None,
              'headers': {'status': '200',
                          'content-length': '0',
                          'date': 'Sun, 13 Sep 2015 07:43:01 GMT',
                          'content-type': 'application/json',
                          'x-openstack-request-id': 'req-2',
                          'vary': 'X-Auth-Token',
                          'connection': 'close',
                          'server': 'Apache/2.4.7 (Ubuntu)'}})])

    def test_body_parse(self):
        result = db_to_call_list(
            tempest_log.parse_logfile(StringIO(SIMPLE_LOG_BODY)))

        self.assertEqual(result, [
            ({'url': '/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1',
              'headers': {'content-type': 'application/json',
                          'content-length': '0',
                          'accept': 'application/json',
                          'x-auth-token': '<omitted>'},
              'body': None,
              'method': 'GET',
              'service': 'compute'},
             {'body': '{\n  "flavor": {\n    "OS-FLV-DISABLED:disabled": false,\n    "OS-FLV-EXT-DATA:ephemeral": 0,\n    "disk": 1,\n    "id": "1",\n    "links": [\n      {\n        "href": "http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1",\n        "rel": "self"\n      },\n      {\n        "href": "http://192.168.122.201:8774/6b45254f6f7c44a1b65ddb8218932226/flavors/1",\n        "rel": "bookmark"\n      }\n    ],\n    "name": "m1.tiny",\n    "os-flavor-access:is_public": true,\n    "ram": 512,\n    "rxtx_factor": 1.0,\n    "swap": "",\n    "vcpus": 1\n  }\n}',  # noqa
              'status_code': '200',
              'headers': {'status': '200', 'content-length': '548',
                          'content-location': 'http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1',  # noqa
                          'x-openstack-nova-api-version': '2.1',
                          'date': 'Sun, 13 Sep 2015 07:43:01 GMT',
                          'vary': 'X-OpenStack-Nova-API-Version',
                          'x-compute-request-id': 'req-959a09e8-3628-419d-964a-1be4ca604232',  # noqa
                          'content-type': 'application/json',
                          'connection': 'close'}})])

    def test_debug_log(self):
        result = db_to_call_list(
            tempest_log.parse_logfile(StringIO(DEBUG_LOG)))

        self.assertEqual(result, [
            ({'body': None,
              'headers': {'accept': 'application/json',
                          'content-type': 'application/json',
                          'content-length': '0',
                          'x-auth-token': '<omitted>'},
              'method': 'DELETE',
              'service': 'application-catalog',
              'url': '/v1/environments/c32c6d5095c4476da549ed065e9b5196'},
             {'body': None,
              'headers': {'connection': 'close',
                          'content-length': '0',
                          'content-type': 'application/json',
                          'date': 'Fri, 04 Sep 2015 15:52:13 GMT',
                          'status': '200',
                          'x-openstack-request-id':
                          'req-0ff36a16-dacd-49c8-9835-7ce92d50f5a7'},
              'status_code': '200'}),
            ({'body': None,
              'headers': {'accept': 'application/json',
                          'content-type': 'application/json',
                          'content-length': '0',
                          'x-auth-token': '<omitted>'},
              'method': 'DELETE',
              'service': 'application-catalog',
              'url': '/v1/environments/7501923609b145ec88eeb4a5c93e371c'
              '/sessions/db214e36e0494c4e9dc67fb0df8548f7'},
             {'body': '403 Forbidden\n'
              'User is not authorized to access these tenant resources\n\n',
              'headers': {'connection': 'close',
                          'content-length': '13',
                          'content-type': 'text/plain; charset=UTF-8',
                          'date': 'Fri, 04 Sep 2015 15:54:42 GMT',
                          'status': '403',
                          'x-openstack-request-id':
                          'req-39c6042e-5a4a-4517-9fe9-32b34cfaa5a8'},
              'status_code': '403'})])

    def test_debug_admin_log(self):
        result = db_to_call_list(
            tempest_log.parse_logfile(StringIO(DEBUG_LOG_AUTH)))

        self.assertEqual(result, [
            ({'body': None,
              'headers': {},
              'method': 'POST',
              'service': 'identity',
              'url': '/v2.0/tokens'},
             {'body': None,
              'headers': {'connection': 'close',
                          'content-length': '0',
                          'content-type': 'application/json',
                          'date': 'Fri, 04 Sep 2015 15:49:42 GMT',
                          'server': 'Apache/2.4.7 (Ubuntu)',
                          'status': '200',
                          'vary': 'X-Auth-Token',
                          'x-openstack-request-id':
                          'req-280bc347-e650-473e-92bb-bcc59103e12c'},
              'status_code': '200'})])
