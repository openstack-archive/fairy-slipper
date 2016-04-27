
List tenants
============

.. rest_method::  GET /v2.0/tenants

Lists tenants to which the token has access.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenants_links: tenants_links
   - enabled: enabled
   - tenants: tenants
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/tenants-list-response.json
   :language: javascript











