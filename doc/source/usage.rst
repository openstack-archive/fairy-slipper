=====
Usage
=====

To configure the API endpoint on a service that uses `routes` as its
routing system.  First look at the config to determine the router
class path.  It can be easily identified in most services `paste.ini`
files by tracing back from the route Using this Murano config you can
see that the URL `/v1` maps to the app `apiv1app`, since this service
uses `routes` you can just copy all class path from the
paste.app_factory line except for the '.factory' part because we don't
want to actually make a router, we just want it to inspect.

::
   
   [composite:rootapp]
   use = egg:Paste#urlmap
   /: apiversions
   /v1: apiv1app
   
   [app:apiversions]
   paste.app_factory = murano.api.versions:create_resource
   
   [app:apiv1app]
   paste.app_factory = murano.api.v1.router:API.factory


So to use fairy-slipper in this project we would add the following to
`api-paste.ini`::

   [composite:rootapp]
   use = egg:Paste#urlmap
   /: apiversions
   /v1: apiv1app
   /docs: fairyslipperapp
   
   [app:apiversions]
   paste.app_factory = murano.api.versions:create_resource
   
   [app:apiv1app]
   paste.app_factory = murano.api.v1.router:API.factory

   [app:fairyslipperapp]
   paste.app_factory = fairy_slipper.app_routes:app_factory
   v1 = murano.api.v1.router:API

And that's it, well in an ideal world it would be, but because of the
flexibility of paste deploy this won't work for Murano unless you also
disable all the middleware other than `request_id faultwrap rootapp`
though, this almost certainly will result in a broken Murano.
