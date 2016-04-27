
List project roles for user in domain
=====================================

.. rest_method::  GET /v3/OS-INHERIT/domains/{domain_id}/users/{user_id}/roles/inherited_to_projects

Lists the project roles that a user inherits from a parent project in a domain.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - domain_id: domain_id






Response Example
----------------

.. literalinclude:: ../samples/OS-INHERIT/user-roles-domain-list-response.json
   :language: javascript



