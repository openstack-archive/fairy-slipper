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

"""

"""

import operator
import textwrap
from pecan import abort, expose
from oslo_log import log as logging
from oslo_serialization import jsonutils
import routes
import webob
import docutils.core


class DocSpecController(object):
    def __init__(self, api):
        self.api = api
        super(DocSpecController, self).__init__()

    @expose(generic=True, template='json')
    def show(self, req):
        routes = {}
        for route in self.api.map.matchlist:
            if 'controller' not in route.defaults:
                continue

            key = (id(route.defaults['controller']),
                   route.defaults['action'])

            controller = route.defaults['controller'].controller
            action = route.defaults['action']

            if not hasattr(controller, action):
                continue

            if route.routepath.endswith('.:(format)'):
                continue

            if key not in routes:
                routes[key] = {'routepath': [],
                               'req': []}

            routes[key]['routepath'] = '/v1' + route.routepath
            routes[key]['req'] = route.reqs
            routes[key]['action'] = action
            routes[key]['conditions'] = route.conditions
            doc = getattr(controller, action).__doc__
            if doc:
                # doc = docutils.core.publish_parts(
                #     textwrap.dedent(doc),
                #     writer=HTMLWriter())['html_body']
                # doc = getattr(controller, action).__doc__
                json = docutils.core.publish_parts(
                    textwrap.dedent(doc),
                    writer=JSONWriter())
                routes[key].update(json['whole']['document'])
            routes[key]['classpath'] = '.'.join(
                [controller.__class__.__module__,
                 controller.__class__.__name__]
            ) + ':' + getattr(controller, action).__name__

        import pdb; pdb.set_trace()  # FIXME
        response = webob.Response()
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        routes = sorted(routes.values(), key=operator.itemgetter('classpath'))
        response.body = jsonutils.dumps(routes)
        return response


def create_resource():
    return wsgi.Resource(DocController())


def create_spec_resource(api):
    return wsgi.Resource(DocSpecController(api))


class DocRouter(base_wsgi.Router):

    @classmethod
    def factory(cls, global_config, **local_config):
        """Simple paste factory, :class:`cinder.wsgi.Router` doesn't have."""
        return cls()

    def __init__(self):
        mapper = routes.Mapper()
        self._setup_api()
        self._setup_routes(mapper)
        super(DocRouter, self).__init__(mapper)

    def _setup_routes(self, mapper):
        mapper.connect('doc', '/', controller=create_resource(),
                       action='show')
        mapper.connect('spec', '/spec',
                       controller=create_spec_resource(self.api),
                       action='show')

    def _setup_api(self):
        raise NotImplementedError
