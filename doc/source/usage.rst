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
able to address these warnings by patching the WADL files. Here are example
patches that fixed what was uncovered in the past:

 * https://review.openstack.org/#/c/213571/ (couldn't find a List flavors method)
 * https://review.openstack.org/#/c/215350/ (couldn't find a /ips method)

To find out which WADL files have issues, run the `migrate.sh` script with
`--verbose-docs`::

    2015-12-01 08:23:14,549 fairy_slipper.cmd.wadl_to_swagger INFO Parsing /Users/annegentle/src/fairy-slipper/api-site/api-ref/src/wadls/netconn-api/src/os-networks.wadl
    2015-12-01 08:23:14,551 fairy_slipper.cmd.wadl_to_swagger WARNING No tags for method listVersionsv2-neutron
    2015-12-01 08:23:14,552 fairy_slipper.cmd.wadl_to_swagger WARNING No tags for method showVersionDetailsv2-neutron

How to build and display API guides
-----------------------------------

Once you have the migrated files, including RST and JSON files, you can run the
web server to display the API reference information.

Prerequisites:

 * npm
 * bower
 
This installs bower into the global system path, which is not ideal. However,
if you run into issues while running the server, you can run these commands::

    sudo npm install -g bower
    bower install installed

To run the web server after getting migrated content with the `migrate.sh`
script, you run the `run_server.sh` script::

    ./run_server.sh

A Pecan-based web server then runs on http://127.0.0.1:8080 in your local
environment.

To see the JSON listing of all documented APIs, go to:
http://127.0.0.1:8080/doc/

Then, you can look at individual REST API URL such as:

"url": "identity/v2/",

by adding identity/v2/ to the local server URL http://127.0.0.1:8080/doc/.

The actual Swagger JSON file is here for inspection once you're running the web
server:

http://127.0.0.1:8080/doc/identity/v2/

If you want to work on the server code (AngularJS) itself, install `grunt` and
you can then view the web server at http://127.0.0.1:9000 (port 9000 instead of
8080) with automatic reloading.

How to author API reference information
---------------------------------------

Once all the WADL information is migrated to the new format, we need to author
API information in a certain format so we can integrate it on the
http://developer.openstack.org pages.

The interim `conversion_files` files are:

 * JSON files containing tags that Sphinx uses to put content together
 * JSON files containing Swagger snippets with all the possible paths from WADL

The basic `api_doc` files are contained in directories per service and version:

 * <servicename>/<version>/v1.rst: contains a listing of each
   GET/PUT/POST/DELETE call as a Sphinx directive  such as `.. http:put::` with
   a title, synopsis, request and response examples pointing to files in the
   `/examples/` directory, accepts and produces info, tag info, request schema,
   and parameters along with documented status codes.
 * <servicename>/<version>/v1-tags.rst: contains the groupings such as API
   versions, that were available in the WADL file. Contains considerable more
   docs and descriptions if that content was originally written in the WADL,
   such as defining backup statuses, for example.
 * <servicename>/<version>/: contains a Swagger-format listing of all calls
   users can get from that service. These JSON files are able to be assembled
   into a longer Swagger file. *

.. note::
   Theoretically, anyway. Have yet to do this re-assembly in practice. Or, the
   Swagger can be hand-written using the Swagger format for an API that
   did not originally have a WADL file migrated. In that case, you would still
   use the file and directory structure described above to have the Angular JS
   app display the content.

How to author API concepts and how-to articles
----------------------------------------------

The landing page at developer.openstack.org is sourced from
https://github.com/openstack/api-site/tree/master/www/index.html. It
is undergoing a revision, but the page currently contains links to SDKs, CLIs,
and API reference information for OpenStack services.

For API articles such as "What are the request and response formats for an API"
or "Server concepts" we can point to the Compute API Guide for example,
published to http://developer.openstack.org/api-guide/compute/ and sourced from
https://github.com/openstack/nova/tree/master/api-guide/source. These articles
are written in RST and built with Sphinx. Each OpenStack project should follow
that pattern for conceptual and how-to information published in articles to
developer.openstack.org.

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
