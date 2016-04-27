
List pools
==========

.. rest_method::  GET /v2.0/lb/pools

Lists pools.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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
   - pools: pools
   - status_description: status_description
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/pools-list-response.json
   :language: javascript








