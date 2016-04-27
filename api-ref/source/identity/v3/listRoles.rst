
List roles
==========

.. rest_method::  GET /v3/roles

Lists roles.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - roles: roles
   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/roles-list-response.json
   :language: javascript










