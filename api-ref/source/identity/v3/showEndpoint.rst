
Show endpoint details
=====================

.. rest_method::  GET /v3/endpoints/{endpoint_id}

Shows details for an endpoint.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - endpoint_id: endpoint_id



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

.. literalinclude:: ../samples/admin/endpoint-show-response.json
   :language: javascript










