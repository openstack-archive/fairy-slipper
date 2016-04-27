
Create service
==============

.. rest_method::  POST /v3/services

Creates a service.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - service: service
   - enabled: enabled
   - service_id: service_id
   - type: type
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/admin/service-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - service: service
   - links: links
   - type: type
   - id: id
   - description: description














