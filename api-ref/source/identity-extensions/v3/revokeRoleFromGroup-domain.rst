
Revoke project role from group in domain
========================================

.. rest_method::  DELETE /v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects

Revokes an inherited project role from a group in a domain.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group_id: group_id
   - role_id: role_id
   - domain_id: domain_id







