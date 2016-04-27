
Assign role to group in domain projects
=======================================

.. rest_method::  PUT /v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects

Assigns a role to a group in projects owned by a domain.

The API applies the inherited role to owned projects, both existing
and future. The inherited role does not appear as a role in a
domain-scoped token.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group_id: group_id
   - role_id: role_id
   - domain_id: domain_id







