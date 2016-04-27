
Update endpoint
===============

.. rest_method::  PATCH /v3/endpoints/{endpoint_id}

Updates an endpoint.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - endpoint: endpoint
   - name: name
   - url: url
   - region: region
   - interface: interface
   - service_id: service_id
   - endpoint_id: endpoint_id

Request Example
---------------

.. literalinclude:: ../samples/admin/endpoint-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - endpoint: endpoint
   - name: name
   - links: links
   - url: url
   - region: region
   - interface: interface
   - service_id: service_id




Response Example
----------------

.. literalinclude:: ../samples/admin/endpoint-update-response.json
   :language: javascript












