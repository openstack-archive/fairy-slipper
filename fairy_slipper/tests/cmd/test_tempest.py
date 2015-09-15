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


SIMPLE_LOG = """Request (FlavorsV2TestJSON:setUpClass): 200 POST http://192.168.122.201:5000/v2.0/tokens
Request - Headers: {}
        Body: None
    Response - Headers: {'status': '200', 'content-length': '2987', 'vary': 'X-Auth-Token', 'server': 'Apache/2.4.7 (Ubuntu)', 'connection': 'close', 'date': 'Sun, 13 Sep 2015 07:43:01 GMT', 'content-type': 'application/json', 'x-openstack-request-id': 'req-1'}
        Body: None
Request (FlavorsV2TestJSON:test_get_flavor): 200 POST http://192.168.122.201:5000/v2.0/tokens
Request - Headers: {}
        Body: None
    Response - Headers: {'status': '200', 'content-length': '2987', 'vary': 'X-Auth-Token', 'server': 'Apache/2.4.7 (Ubuntu)', 'connection': 'close', 'date': 'Sun, 13 Sep 2015 07:43:01 GMT', 'content-type': 'application/json', 'x-openstack-request-id': 'req-2'}
        Body: None
"""  # noqa

SIMPLE_LOG_BODY = """Request (FlavorsV2TestJSON:test_get_flavor): 200 GET http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1 0.117s
Request - Headers: {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-Auth-Token': '<omitted>'}
        Body: None
    Response - Headers: {'status': '200', 'content-length': '430', 'content-location': 'http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1', 'x-compute-request-id': 'req-959a09e8-3628-419d-964a-1be4ca604232', 'vary': 'X-OpenStack-Nova-API-Version', 'connection': 'close', 'x-openstack-nova-api-version': '2.1', 'date': 'Sun, 13 Sep 2015 07:43:01 GMT', 'content-type': 'application/json'}
        Body: {"flavor": {"name": "m1.tiny", "links": [{"href": "http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1", "rel": "self"}, {"href": "http://192.168.122.201:8774/6b45254f6f7c44a1b65ddb8218932226/flavors/1", "rel": "bookmark"}], "ram": 512, "OS-FLV-DISABLED:disabled": false, "vcpus": 1, "swap": "", "os-flavor-access:is_public": true, "rxtx_factor": 1.0, "OS-FLV-EXT-DATA:ephemeral": 0, "disk": 1, "id": "1"}}
"""  # noqa


class TestLogParser(unittest.TestCase):
    def test_simple_parse(self):
        result = tempest_log.parse_logfile(StringIO(SIMPLE_LOG))
        self.assertEqual(result, [
            ({'url': '/v2.0/tokens',
              'service': 'identity',
              'headers': {},
              'body': None,
              'method': 'POST'},
             {'status_code': '200',
              'body': None,
              'headers': {'status': '200',
                          'content-length': '2987',
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
                          'content-length': '2987',
                          'date': 'Sun, 13 Sep 2015 07:43:01 GMT',
                          'content-type': 'application/json',
                          'x-openstack-request-id': 'req-2',
                          'vary': 'X-Auth-Token',
                          'connection': 'close',
                          'server': 'Apache/2.4.7 (Ubuntu)'}})])

    def test_body_parse(self):
        result = tempest_log.parse_logfile(StringIO(SIMPLE_LOG_BODY))

        self.assertEqual(result, [
            ({'url': '/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1',
              'headers': {'Content-Type': 'application/json',
                          'Accept': 'application/json',
                          'X-Auth-Token': '<omitted>'},
              'body': None,
              'method': 'GET',
              'service': 'compute'},
             {'body': '{\n  "flavor": {\n    "OS-FLV-DISABLED:disabled": false, \n    "OS-FLV-EXT-DATA:ephemeral": 0, \n    "disk": 1, \n    "id": "1", \n    "links": [\n      {\n        "href": "http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1", \n        "rel": "self"\n      }, \n      {\n        "href": "http://192.168.122.201:8774/6b45254f6f7c44a1b65ddb8218932226/flavors/1", \n        "rel": "bookmark"\n      }\n    ], \n    "name": "m1.tiny", \n    "os-flavor-access:is_public": true, \n    "ram": 512, \n    "rxtx_factor": 1.0, \n    "swap": "", \n    "vcpus": 1\n  }\n}',  # noqa
              'status_code': '200',
              'headers': {'status': '200', 'content-length': '430',
                          'content-location': 'http://192.168.122.201:8774/v2.1/6b45254f6f7c44a1b65ddb8218932226/flavors/1',  # noqa
                          'x-openstack-nova-api-version': '2.1',
                          'date': 'Sun, 13 Sep 2015 07:43:01 GMT',
                          'vary': 'X-OpenStack-Nova-API-Version',
                          'x-compute-request-id': 'req-959a09e8-3628-419d-964a-1be4ca604232',  # noqa
                          'content-type': 'application/json',
                          'connection': 'close'}})])
