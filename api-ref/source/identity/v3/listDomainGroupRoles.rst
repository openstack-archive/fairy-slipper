
List roles for group on domain
==============================

.. rest_method::  GET /v3/domains/{domain_id}/groups/{group_id}/roles

Lists roles for a group on a domain.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - group_id: group_id






Response Example
----------------

.. literalinclude:: ../samples/admin/domain-group-roles-list-response.json
   :language: javascript










