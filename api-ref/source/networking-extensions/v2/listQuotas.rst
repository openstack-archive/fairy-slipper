
List quotas for tenants with non-default quota values
=====================================================

.. rest_method::  GET /v2.0/quotas

Lists quotas for tenants who have non-default quota values.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - subnet: subnet
   - network: network
   - floatingip: floatingip
   - subnetpool: subnetpool
   - quotas: quotas
   - security_group_rule: security_group_rule
   - security_group: security_group
   - router: router
   - rbac_policy: rbac_policy
   - port: port




Response Example
----------------

.. literalinclude:: ../samples/quotas/quotas-list-response.json
   :language: javascript





