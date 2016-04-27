
List listeners
==============

.. rest_method::  GET /v2.0/lbaas/listeners

Lists all listeners.

This operation lists all listeners that are associated with your
tenant account.

The list might be empty.

Example: List listeners


Normal response codes: 200
Error response codes:500,401,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - protocol_port: protocol_port
   - protocol: protocol
   - description: description
   - default_tls_container_ref: default_tls_container_ref
   - admin_state_up: admin_state_up
   - loadbalancers: loadbalancers
   - tenant_id: tenant_id
   - sni_container_refs: sni_container_refs
   - connection_limit: connection_limit
   - listeners: listeners
   - default_pool_id: default_pool_id
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/listeners-list-response.json
   :language: javascript






