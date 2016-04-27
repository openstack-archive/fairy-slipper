
Show load balancer details
==========================

.. rest_method::  GET /v2.0/lbaas/loadbalancers/{loadbalancer_id}

Shows details for a load balancer.

This operation returns a load balancer object, by ID. If you are
not an administrative user and the load balancer object does not
belong to your tenant account, the service returns the HTTP
``Forbidden (403)`` response code.


Normal response codes: 200
Error response codes:404,403,500,401,413,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - provisioning_status: provisioning_status
   - listeners: listeners
   - vip_address: vip_address
   - operating_status: operating_status
   - provider: provider
   - vip_subnet_id: vip_subnet_id
   - flavor: flavor
   - id: id
   - loadbalancer: loadbalancer
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/loadbalancer-show-response.json
   :language: javascript










