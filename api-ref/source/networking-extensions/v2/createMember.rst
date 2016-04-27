
Create a load balancer member
=============================

.. rest_method::  POST /v2.0/lb/members

Creates a load balancer member.

Error response codes:201,400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - weight: weight
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - pool_id: pool_id
   - member: member
   - address: address
   - protocol_port: protocol_port

Request Example
---------------

.. literalinclude:: ../samples/lbaas/member-create-request.json
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










