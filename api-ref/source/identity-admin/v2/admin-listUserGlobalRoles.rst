
List user global roles
======================

.. rest_method::  GET /v2.0/users/{userId}/roles

Lists global roles for a user. Excludes tenant roles.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - userId: userId



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - roles_links: roles_links
   - roles: roles
   - description: description
   - name: name
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/admin/roles-list-response.json
   :language: javascript











