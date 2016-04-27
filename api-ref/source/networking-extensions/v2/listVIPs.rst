
List VIPs
=========

.. rest_method::  GET /v2.0/lb/vips

Lists VIPs.

The list might be empty.


Normal response codes: 200
Error response codes:500,401,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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
   - address: address
   - vips: vips
   - protocol_port: protocol_port
   - port_id: port_id
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/vips-list-response.json
   :language: javascript






