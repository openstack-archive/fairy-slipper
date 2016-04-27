
Assign role to user owned by domain projects
============================================

.. rest_method::  PUT /v3/OS-INHERIT/domains/{domain_id}/users/{user_id}/roles/{role_id}/inherited_to_projects

Assigns a role to a user in projects owned by a domain.

The API applies the inherited role to the existing and future owned
projects. The inherited role does not appear as a role in a domain-
scoped token.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - role_id: role_id
   - domain_id: domain_id







