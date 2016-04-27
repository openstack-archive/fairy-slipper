
List roles for user on domain
=============================

.. rest_method::  GET /v3/domains/{domain_id}/users/{user_id}/roles

Lists roles for a user on a domain.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - user_id: user_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - roles: roles
   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/domain-user-roles-list-response.json
   :language: javascript










