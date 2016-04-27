
List roles for user
===================

.. rest_method::  GET /v2.0/tenants/{tenantId}/users/{userId}/roles

Lists roles for a user on a tenant. Excludes global roles.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - userId: userId
   - tenantId: tenantId



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











