
Revoke role from user on domain
===============================

.. rest_method::  DELETE /v3/domains/{domain_id}/users/{user_id}/roles/{role_id}

Revokes a role from a user on a domain.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - role_id: role_id
   - user_id: user_id
















