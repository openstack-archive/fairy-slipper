
List domains
============

.. rest_method::  GET /v3/domains

Lists all domains.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - enabled: enabled



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - links: links
   - enabled: enabled
   - domains: domains
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/admin/domains-list-response.json
   :language: javascript










