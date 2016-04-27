
Create a load balancer VIP
==========================

.. rest_method::  POST /v2.0/lb/vips

Creates a load balancer VIP.

Error response codes:201,400,404,500,401,413,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - protocol: protocol
   - description: description
   - admin_state_up: admin_state_up
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - connection_limit: connection_limit
   - pool_id: pool_id
   - session_persistence: session_persistence
   - vip: vip
   - address: address
   - protocol_port: protocol_port
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/lbaas/vip-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - status_description: status_description
   - protocol: protocol
   - description: description
   - admin_state_up: admin_state_up
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - connection_limit: connection_limit
   - pool_id: pool_id
   - session_persistence: session_persistence
   - vip: vip
   - address: address
   - protocol_port: protocol_port
   - port_id: port_id
   - id: id
   - name: name












