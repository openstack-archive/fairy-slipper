
Show listener details
=====================

.. rest_method::  GET /v2.0/lbaas/listeners/{listener_id}

Shows details for a listener.

This operation returns a listener object, by ID. If you are not an
administrative user and the listener object does not belong to your
account, the API returns the HTTP ``Forbidden (403)`` response
code.

Example: Show listener details


Normal response codes: 200
Error response codes:404,403,500,401,413,503,409,


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
   - listener: listener
   - default_pool_id: default_pool_id
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/listener-show-response.json
   :language: javascript










