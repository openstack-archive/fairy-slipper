
Check whether user has role on domain
=====================================

.. rest_method::  HEAD /v3/domains/{domain_id}/users/{user_id}/roles/{role_id}

Validates that a user has a role on a domain.

Error response codes:204,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - role_id: role_id
   - user_id: user_id














