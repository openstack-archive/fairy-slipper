
Revoke project role from user in domain
=======================================

.. rest_method::  DELETE /v3/OS-INHERIT/domains/{domain_id}/users/{user_id}/roles/{role_id}/inherited_to_projects

Revokes an inherited project role from a user in a domain.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - role_id: role_id
   - domain_id: domain_id







