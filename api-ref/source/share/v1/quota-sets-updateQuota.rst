
Update quotas
=============

.. rest_method::  PUT /v2/{tenant_id}/quota-sets/{tenant_id}

Updates quotas for a tenant.

If you specify the optional ``user_id`` query parameter, you update
the quotas for this user in the tenant. If you omit this parameter,
you update the quotas for the project.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - force: force
   - gigabytes: gigabytes
   - snapshots: snapshots
   - snapshot_gigabytes: snapshot_gigabytes
   - shares: shares
   - share_networks: share_networks
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-quota-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - gigabytes: gigabytes
   - snapshots: snapshots
   - snapshot_gigabytes: snapshot_gigabytes
   - shares: shares
   - quota_set: quota_set
   - share_networks: share_networks




Response Example
----------------

.. literalinclude:: ../samples/manila-quota-update-response.json
   :language: javascript



