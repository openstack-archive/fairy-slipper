========
Usage
========

To use fairy-slipper in a project add the following to `api-paste.ini`::

   [composite:osapi_volume]
   use = call:cinder.api:root_app_factory
   /: apiversions
   /v1: openstack_volume_api_v1
   /v2: openstack_volume_api_v2
   /docs: openstack_volume_doc

   [pipeline:openstack_volume_doc]
   pipeline = docs


   [app:docs]
   paste.app_factory = fairy_slipper.cinder:app_factory
   v1 = cinder.api.v1.router:APIRouter
   v2 = cinder.api.v2.router:APIRouter
