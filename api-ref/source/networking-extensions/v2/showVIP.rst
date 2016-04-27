
Show VIP details
================

.. rest_method::  GET /v2.0/lb/vips/{vip_id}

Shows details for a VIP.


Normal response codes: 200
Error response codes:404,403,500,401,413,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - vip_id: vip_id



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




Response Example
----------------

.. literalinclude:: ../samples/lbaas/vip-show-response.json
   :language: javascript










