
Show quotas
===========

.. rest_method::  GET /v2/{tenant_id}/quota-sets/{tenant_id}

Shows quotas for a tenant.

If you specify the optional ``user_id`` query parameter, you get
the quotas for this user in the tenant. If you omit this parameter,
you get the quotas for the project.


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



