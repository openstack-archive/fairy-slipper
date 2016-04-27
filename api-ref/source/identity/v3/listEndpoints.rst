
List endpoints
==============

.. rest_method::  GET /v3/endpoints

Lists all available endpoints.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - interface: interface
   - service_id: service_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - region_id: region_id
   - links: links
   - url: url
   - region: region
   - enabled: enabled
   - interface: interface
   - service_id: service_id
   - endpoints: endpoints
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/admin/endpoints-list-response.json
   :language: javascript










