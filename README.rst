=============
fairy-slipper
=============

A project to make OpenStack API's self documententing.

* Free software: Apache license
* Documentation: doc/source directory
* Source: https://git.openstack.org/cgit/openstack/fairy-slipper
* Bugs: https://bugs.launchpad.net/openstack-api-site

Features
--------

* Migrates WADL source to Swagger files
* Provides display of RST plus Swagger JSON files in a web browser

Development
-----------

First run the migrate script to initially migrate the content from wadl::

  ./migrate.sh

This script will checkout the current version of the documentation.

To run the webserver use::

  ./run_server.sh

A Pecan based webserver will then listen on http://127.0.0.1:8080

AngularJS
~~~~~~~~~

To develop the AngularJS component, it's easiest if you use the grunt webserver::

  grunt

You will still need to run the Fairy-Slipper webserver, but this will
enable auto reloading if you visit the port http://127.0.0.1:9000

Directory Structure (Future)
----------------------------

Current documentation output layout::

   api-doc/ -- the root of the documentation
   api-doc/index.json  -- the index file that lists all the files that are included in the API doc.
   api-doc/<service>/<version>.rst
   api-doc/<service>/<version>/<request_schema>.json
   api-doc/<service>/<version>/<response_schema>_<status_code>.json
   api-doc/<service>/<version>/examples/<request>_req.json
   api-doc/<service>/<version>/examples/<response>_resp_<status_code>.json
   conversion_files_valid/<service-version>.json -- valid Swagger files

Other Swagger UIs
-----------------

Taken from https://github.com/swagger-api/swagger-spec/wiki/Sites-and-Services

- http://docs.apimatic.apiary.io/
- http://docs.api2cart.com/post/interactive-docs
- http://chat.banckle.com/api/v3.0/
- http://www.evercam.io/develop/docs
- https://api.elastic.io/docs/
- https://developer.concur.com/
- https://www.callfire.com/api-documentation/rest/version/1.1
- https://www.bitmex.com/api/explorer/
- https://bitdango.com/api
- https://api.groupdocs.com/v2.0/spec/
- http://developer.wordnik.com/docs.html
- https://api.sensr.net/doc/v3/index.html

Other API documentation Tools
-----------------------------

- https://github.com/danielgtaylor/aglio

Alternative Clients
-------------------

- https://github.com/Orange-OpenSource/angular-swagger-ui
- https://github.com/apigee-127/swagger-client-API
- https://github.com/signalfx/swagger-ajax-client/
- https://github.com/signalfx/swagger-angular-client
- https://github.com/signalfx/swagger-client-generator


Other Useful Tools
------------------

- http://jsonschema.net/
