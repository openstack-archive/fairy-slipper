
List project roles for group in domain
======================================

.. rest_method::  GET /v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/inherited_to_projects

Lists the project roles that a group inherits from a parent project in a domain.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group_id: group_id
   - domain_id: domain_id






Response Example
----------------

.. literalinclude:: ../samples/OS-INHERIT/group-roles-domain-list-response.json
   :language: javascript



