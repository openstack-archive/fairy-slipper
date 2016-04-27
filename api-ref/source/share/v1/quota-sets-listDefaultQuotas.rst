
Show default quotas
===================

.. rest_method::  GET /v2/{tenant_id}/quota-sets/{tenant_id}/defaults

Shows default quotas for a tenant.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - gigabytes: gigabytes
   - shares: shares
   - snapshot_gigabytes: snapshot_gigabytes
   - snapshots: snapshots
   - quota_set: quota_set
   - id: id
   - share_networks: share_networks




Response Example
----------------

.. literalinclude:: ../samples/manila-quota-show-response.json
   :language: javascript



