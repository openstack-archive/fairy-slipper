import operator
import textwrap
from pecan import expose
from paste.deploy import util as paste_util
from pecan.hooks import HookController
import docutils.core

from fairy_slipper.rest import JSONWriter
from fairy_slipper import hooks

routes = {}


class VersionAPIController(object):

    def __init__(self, versions):
        self.versions = versions

    @expose()
    def _lookup(self, id_, *remainder):
        if id_ in self.versions:
            return DocSpecController(self.versions[id_]), remainder

    @expose(generic=True, template='json')
    def index(self):
        return self.versions.keys()


class DocSpecController(HookController):

    __hooks__ = [hooks.CORSHook()]

    def __init__(self, router):
        self.api = paste_util.lookup_object(router)()
        super(DocSpecController, self).__init__()

    @expose(generic=True, template='json')
    def index(self):
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
                json = docutils.core.publish_parts(
                    textwrap.dedent(doc),
                    writer=JSONWriter())
                routes[key].update(json['whole']['document'])
            routes[key]['classpath'] = '.'.join(
                [controller.__class__.__module__,
                 controller.__class__.__name__]
            ) + ':' + getattr(controller, action).__name__

        routes = sorted(routes.values(),
                        key=operator.itemgetter('classpath'))
        return routes
