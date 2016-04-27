
Create endpoint
===============

.. rest_method::  POST /v3/endpoints

Creates an endpoint.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - endpoint: endpoint
   - name: name
   - url: url
   - enabled: enabled
   - interface: interface
   - service_id: service_id
   - region_id: region_id

Request Example
---------------

.. literalinclude:: ../samples/admin/endpoint-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - endpoint: endpoint
   - name: name
   - links: links
   - url: url
   - region: region
   - enabled: enabled
   - interface: interface
   - service_id: service_id
   - id: id
   - region_id: region_id














