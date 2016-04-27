
List services
=============

.. rest_method::  GET /v3/services

Lists all services.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - type: type



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - links: links
   - enabled: enabled
   - services: services
   - type: type
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/admin/services-list-response.json
   :language: javascript










