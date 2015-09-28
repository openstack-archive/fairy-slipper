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

import itertools
import json
import logging
from os import path

import docutils.core
from pecan import conf
from pecan import expose
from pecan import response
from webob.exc import status_map
from webob.static import FileIter

from fairy_slipper import hooks
from fairy_slipper.rest import JSONWriter

logger = logging.getLogger(__name__)


class JSONFileController(object):

    __hooks__ = [hooks.CORSHook()]

    def __init__(self, filepath):
        self.filepath = filepath

    @expose('json')
    @expose(content_type='text/plain')
    def _default(self):
        if path.exists(self.filepath + '.json'):
            self.filepath = self.filepath + '.json'
        if path.exists(self.filepath + '.txt'):
            self.filepath = self.filepath + '.txt'
        if not path.exists(self.filepath):
            response.status = 404
            return response
        response.app_iter = FileIter(open(self.filepath, 'rb'))
        return response


class DocController(object):

    __hooks__ = [hooks.CORSHook()]

    def __init__(self, service_path, service_info):
        self.service_info = service_info
        base_filepath = path.join(conf.app.api_doc, service_path.rstrip('/'))
        self.api_rst = base_filepath + '.rst'
        self.tags_rst = base_filepath + '-tags.rst'
        self.examples_dir = path.join(base_filepath, 'examples') + path.sep
        self.schema_dir = base_filepath + path.sep
        if not path.exists(self.api_rst):
            logger.warning("Can't find ReST API doc at %s", self.api_rst)
        if not path.exists(self.tags_rst):
            logger.warning("Can't find ReST TAG doc at %s", self.tags_rst)

    @expose('json')
    def index(self):
        if path.exists(self.tags_rst) and path.exists(self.api_rst):
            rst = open(self.api_rst).read() + \
                "\n\n" + open(self.tags_rst).read()
        elif path.exists(self.api_rst):
            rst = open(self.api_rst).read()
        else:
            logger.warning("Can't find ReST documents to render.")
            return {}

        json = docutils.core.publish_string(rst, writer=JSONWriter())

        return {'info': self.service_info,
                'paths': json['paths'],
                'tags': json['tags']}

    @expose()
    def _lookup(self, *components):
        if len(components) != 2 and len(components) != 3:
            return

        if components[0] == 'examples':
            example = components[1]
            filepath = path.join(self.examples_dir, example)
            return JSONFileController(filepath), []
        else:
            filename = components[0]
            print(filename)
            filepath = path.join(self.schema_dir, filename)
            return JSONFileController(filepath), []


class ServicesController(object):

    def __init__(self):
        filepath = path.join(conf.app.api_doc, 'index.json')
        self.url_map = {}
        if not path.exists(filepath):
            logger.error("Can't find documentation at %s", filepath)
            self.services_info = {}
            return
        try:
            self.services_info = json.load(open(filepath))
        except ValueError:
            logger.error("Failed to load %s", filepath)
            raise
        for key, info in self.services_info.items():
            # Add the path into each element, this is to make
            # consumption by the JS client easier.
            info['url'] = key

            current_map = self.url_map
            previous_map = None
            for part in [k for k in key.split('/') if k]:
                if part not in current_map:
                    current_map[part] = {}
                previous_map = current_map
                current_map = current_map[part]
            else:
                previous_map[part] = DocController(key, info)

    @expose('json')
    def index(self):
        return self.services_info.values()

    @expose('json')
    def _lookup(self, *components):
        url_map = self.url_map
        url_walk = itertools.chain(components)
        for component in url_walk:
            if component in url_map:
                url_map = url_map[component]
            else:
                break
            if isinstance(url_map, DocController):
                return url_map, [u for u in url_walk]


class RootController(object):

    def __init__(self):
        self.doc = ServicesController()

    @expose(content_type='text/html')
    def index(self):
        filepath = path.join(conf.app.static_root, 'index.html')
        f = open(filepath, 'rb')
        response.app_iter = FileIter(f)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:
            status = 0
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
