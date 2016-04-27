
Update listener
===============

.. rest_method::  PUT /v2.0/lbaas/listeners/{listener_id}

Updates a listener.

This operation updates the attributes of a listener. Upon
successful validation of the request, the service returns the HTTP
``Accepted (202)`` response code.

Note: You cannot update the ``listener_id``, ``tenant_id``,
``loadbalancer_id``, ``loadbalancers``, ``default_pool_id``,
``protocol``, and ``protocol_port`` attributes. Attempting to
update an immutable attribute results in the HTTP ``Immutable
(422)`` response code.

Note: You cannot update a listener if the load balancer to which
the listener is attached does not have an ``ACTIVE`` provisioning
status.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - protocol_port: protocol_port
   - protocol: protocol
   - description: description
   - default_tls_container_ref: default_tls_container_ref
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - sni_container_refs: sni_container_refs
   - connection_limit: connection_limit
   - listener: listener
   - default_pool_id: default_pool_id
   - loadbalancer_id: loadbalancer_id
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/lbaas/listener-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/lbaas/listener-update-response.json
   :language: javascript








