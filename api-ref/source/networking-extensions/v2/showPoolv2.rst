
Show pool details
=================

.. rest_method::  GET /v2.0/lbaas/pools/{pool_id}

Shows details for a pool.

This operation shows details for a pool, by ID. If you are not an
administrative user and the pool object does not belong to your
tenant account, the call returns the HTTP ``Forbidden (403)``
response code.

If this operation succeeds, it returns a ``pool`` element.

Example: Show pool details


Normal response codes: 200
Error response codes:404,403,500,401,413,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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

.. literalinclude:: ../samples/lbaas/pool-show-response.json
   :language: javascript










