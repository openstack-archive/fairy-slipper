
List members
============

.. rest_method::  GET /v2.0/lb/members

Lists members.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - status_description: status_description
   - weight: weight
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - pool_id: pool_id
   - members: members
   - address: address
   - protocol_port: protocol_port
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/lbaas/members-list-response.json
   :language: javascript








