
List quotas for a tenant
========================

.. rest_method::  GET /v2.0/quotas/{tenant_id}

Lists quotas for a tenant.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



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

.. literalinclude:: ../samples/quotas/quotas-list-for-tenant-response.json
   :language: javascript






