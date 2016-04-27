
List load balancers
===================

.. rest_method::  GET /v2.0/lbaas/loadbalancers

Lists all load balancers for the tenant account.

The list might be empty.


Normal response codes: 200
Error response codes:404,500,401,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - admin_state_up: admin_state_up
   - loadbalancers: loadbalancers
   - tenant_id: tenant_id
   - provisioning_status: provisioning_status
   - listeners: listeners
   - vip_address: vip_address
   - provider: provider
   - vip_subnet_id: vip_subnet_id
   - flavor: flavor
   - id: id
   - operating_status: operating_status
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/loadbalancers-list-response.json
   :language: javascript







