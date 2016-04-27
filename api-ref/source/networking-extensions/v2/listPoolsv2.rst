
List pools
==========

.. rest_method::  GET /v2.0/lbaas/pools

Lists all pools that are associated with your tenant account.

The list might be empty.

Example: List pools


Normal response codes: 200
Error response codes:500,401,503,


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

.. literalinclude:: ../samples/lbaas/pools-list-response.json
   :language: javascript






