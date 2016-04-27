
Create a load balancer pool
===========================

.. rest_method::  POST /v2.0/lb/pools

Creates a load balancer pool.

Error response codes:201,400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - lb_method: lb_method
   - protocol: protocol
   - description: description
   - admin_state_up: admin_state_up
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - pool: pool
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/lbaas/pool-create-request.json
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










