======
How to
======

This page offers a collection of use cases for how to use this tool to maintain
API guides using this framework, and describes best practices to give the API
consumers information they need to get their tasks done.

How to migrate existing WADL
----------------------------

The fairy-slipper repository contains a migration script that retrieves the
WADL source from the openstack/api-site/ repository and then converts the WADL
to RST plus JSON files.

The use for that script is to run it from the root of the fairy-slipper
directory, using -V to create a virtualenv if one doesn't already exist::

  ./migrate.sh

The script has some options for the level of migration:

--docs-only              Only install fairy-slipper and the api-site clone
--verbose-docs           Verbose logging of document generation
--docbkx2json            Only perform docbookx to json conversion
--wadl2swagger           Only perform wadl to swagger conversion
--swagger2rst            Only perform swagger to rst conversion

The full migration outputs all files to a `api_doc` directory.

The interim migrations output files to a `conversions_files` directory. For
example, if you run with --wadl2swagger you can see Swagger JSON reference
files in `conversion_files`.

The `api_doc` output is organized by service in directories, such as
`blockstorage` and `compute`.

You may see warnings logged, such as::

2015-11-30 14:57:13,946 fairy_slipper.cmd.wadl_to_swagger WARNING Can't find method listFlavors
2015-11-30 14:57:14,377 fairy_slipper.cmd.wadl_to_swagger WARNING No tags for method getServerAddresses

That means that the WADL itself has an unclear definition. So far we have been
able to address these warnings by patching the WADL files.

How to build and display API guides
-----------------------------------


How to author API reference information
---------------------------------------


How to author API concepts and how-to articles
----------------------------------------------



How to generate API reference outlines from code
------------------------------------------------

You can configure the API endpoint on a service that uses `routes` as its
routing system to generate API reference information using this tool.
First look at the config to determine the router class path. It can be easily
identified in most services `paste.ini` files by tracing back from the route.

As an example, using this Murano config you can see that the URL `/v1` maps to
the app `apiv1app`, and since this service uses `routes` you can just copy all
class path from the paste.app_factory line except for the '.factory' part.
Copying these paths makes sense because we don't want to make a router, we
simply want it so we can inspect it.

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

And that's it, well in an ideal world it would be. However, because of the
flexibility of paste deploy this configuration as-is won't work for a running
instance of Murano. You would have to also disable all the middleware other
than `request_id faultwrap rootapp`, though, this almost certainly will result
in a broken Murano service. So, for the purposes of creating an outline, or for
ensuring completeness of the API docs starting point, you could change the
`api-paste.ini` for the purposes of inspection only.

Note that the file `controllers/routes_inspector.py` in fairy-slipper is
written to match the Murano example. If your service has a different factory
method, you could change fairy-slipper to match.
