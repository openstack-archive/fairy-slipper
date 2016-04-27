
Update quota for a tenant
=========================

.. rest_method::  PUT /v2.0/quotas/{tenant_id}

Updates quotas for a tenant. Use when non-default quotas are desired.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - subnet: subnet
   - network: network
   - floatingip: floatingip
   - subnetpool: subnetpool
   - quota: quota
   - security_group_rule: security_group_rule
   - security_group: security_group
   - router: router
   - rbac_policy: rbac_policy
   - port: port
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/quotas/quotas-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - subnet: subnet
   - network: network
   - floatingip: floatingip
   - subnetpool: subnetpool
   - quota: quota
   - security_group_rule: security_group_rule
   - security_group: security_group
   - router: router
   - rbac_policy: rbac_policy
   - port: port




Response Example
----------------

.. literalinclude:: ../samples/quotas/quotas-update-response.json
   :language: javascript






