from pecan import make_app
from fairy_slipper.controllers import routes


def setup_app(local_conf):
    return make_app(
        routes.VersionAPIController(local_conf),
    )


def app_factory(global_config, **local_conf):
    return setup_app(local_conf=local_conf)
