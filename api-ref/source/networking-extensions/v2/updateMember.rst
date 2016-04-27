
Update member
=============

.. rest_method::  PUT /v2.0/lb/members/{member_id}

Updates a load balancer member.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - member: member
   - pool_id: pool_id
   - weight: weight
   - admin_state_up: admin_state_up
   - member_id: member_id

Request Example
---------------

.. literalinclude:: ../samples/lbaas/member-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - status_description: status_description
   - weight: weight
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - pool_id: pool_id
   - member: member
   - address: address
   - protocol_port: protocol_port
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/lbaas/member-update-response.json
   :language: javascript








