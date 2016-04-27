
Check project role for user in domain
=====================================

.. rest_method::  HEAD /v3/OS-INHERIT/domains/{domain_id}/users/{user_id}/roles/{role_id}/inherited_to_projects

Checks whether a user has an inherited project role in a domain.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - role_id: role_id
   - domain_id: domain_id






Response Example
----------------

.. literalinclude:: 
   :language: javascript



