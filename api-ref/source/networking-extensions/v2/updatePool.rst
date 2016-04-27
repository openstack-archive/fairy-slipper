
Update pool
===========

.. rest_method::  PUT /v2.0/lb/pools/{pool_id}

Updates a load balancer pool.


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
   - pool_id: pool_id

Request Example
---------------

.. literalinclude:: ../samples/lbaas/pool-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - lb_algorithm: lb_algorithm
   - status: status
   - protocol: protocol
   - description: description
   - health_monitors: health_monitors
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - admin_state_up: admin_state_up
   - vip_id: vip_id
   - health_monitors_status: health_monitors_status
   - members: members
   - provider: provider
   - status_description: status_description
   - id: id
   - pool: pool
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/pool-update-response.json
   :language: javascript








