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


from fairy_slipper.tests import FunctionalTest


class TestRootControllerNegative(FunctionalTest):

    def setUp(self):
        self.CONFIG['app']['api_doc'] = \
            '%(confdir)s/fairy_slipper/tests/api_doc_missing'
        super(TestRootControllerNegative, self).setUp()

    def test_get_doc_index(self):
        response = self.app.get('/doc/')
        assert response.json == []
        assert response.status_int == 200


class TestRootController(FunctionalTest):

    def test_get(self):
        response = self.app.get('/')
        assert response.status_int == 200

    def test_search(self):
        response = self.app.post('/', params={'q': 'RestController'})
        assert response.status_int == 200

    def test_get_not_found(self):
        response = self.app.get('/a/bogus/url', expect_errors=True)
        assert response.status_int == 404

    def test_get_doc_index(self):
        response = self.app.get('/doc/')
        assert response.json == [
            {'url': 'identity/v2/',
             'version': 'v2',
             'license': {
                 'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
                 'name': 'Apache 2.0'},
             'service': 'identity',
             'title': 'Identity'}]
        assert response.status_int == 200

    def test_get_doc_identity(self):
        response = self.app.get('/doc/identity/', expect_errors=True)
        assert response.status_int == 404

    def test_get_doc_identity_v2(self):
        response = self.app.get('/doc/identity/v2/')
        assert response.json == \
            {'info':
             {'url': 'identity/v2/',
              'version': 'v2',
              'license': {
                  'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
                  'name': 'Apache 2.0'},
              'service': 'identity',
              'title': 'Identity'},
             'paths': {'/': [{'responses': {},
                              'parameters': [],
                              'produces': [],
                              'consumes': [],
                              'tags': ['simple'],
                              'summary': '',
                              'title': 'Simple route',
                              'method': 'get',
                              'description': ''}]},
             'tags': [{'description': '',
                       'name': 'simple',
                       'summary': 'Simple Tag'}]}
        assert response.status_int == 200
