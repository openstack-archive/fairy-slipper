
Check project role for group in domain
======================================

.. rest_method::  HEAD /v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects

Checks whether a group has an inherited project role in a domain.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group_id: group_id
   - role_id: role_id
   - domain_id: domain_id






Response Example
----------------

.. literalinclude:: 
   :language: javascript



