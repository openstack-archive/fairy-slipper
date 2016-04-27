
Show service details
====================

.. rest_method::  GET /v3/services/{service_id}

Shows details for a service.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_id: service_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - service: service
   - links: links
   - type: type
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/admin/service-show-response.json
   :language: javascript










