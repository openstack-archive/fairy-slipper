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

import copy
from unittest import TestCase

from pecan import set_config
from pecan.testing import load_test_app

__all__ = ['FunctionalTest']


class FunctionalTest(TestCase):
    """Used for functional tests

    Provides a literal application and for testing its integration
    with the framework.
    """
    CONFIG = {
        'server': {
            'port': '8080',
            'host': '0.0.0.0'
        },
        'app': {
            'root': 'fairy_slipper.controllers.root.RootController',
            'modules': ['fairy_slipper'],
            'static_root': '%(confdir)s/public',
            'api_doc': '%(confdir)s/fairy_slipper/tests/api_doc_fixture',
            'template_path': '%(confdir)s/templates',
            'debug': True,
            'errors': {
                '404': '/error/404',
                '__force_dict__': True
            }
        }}

    def __init__(self, *args, **kwargs):
        self.CONFIG = copy.deepcopy(self.CONFIG)
        super(FunctionalTest, self).__init__(*args, **kwargs)

    def setUp(self):
        self.app = load_test_app(copy.deepcopy(self.CONFIG))

    def tearDown(self):
        set_config({}, overwrite=True)
