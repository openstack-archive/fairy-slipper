
Update pool
===========

.. rest_method::  PUT /v2.0/lbaas/pools/{pool_id}

Updates a pool.

This operation updates the attributes of a pool. Upon successful
validation of the request, the service returns the HTTP ``Accepted
(202)`` response code.

Note: You cannot update the pool UUID, ``tenant_id``,
``listener_id``, ``listeners``, ``health_monitor_id``,
``protocol``, and ``members`` immutable attributes. If you try to
update any of these attributes, the service returns the HTTP
``Immutable (422)`` response code.

Note: You cannot update a pool if the load balancer to which it is
attached does not have an ``ACTIVE`` provisioning status.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - pool: pool
   - lb_method: lb_method
   - description: description
   - name: name
   - admin_state_up: admin_state_up

Request Example
---------------

.. literalinclude:: ../samples/lbaas/pool-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - lb_method: lb_method
   - protocol: protocol
   - description: description
   - health_monitors: health_monitors
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - admin_state_up: admin_state_up
   - vip_id: vip_id
   - members: members
   - pools: pools
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/pool-update-response.json
   :language: javascript








