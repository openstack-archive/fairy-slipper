
Force-delete share snapshot
===========================

.. rest_method::  POST /v2/{tenant_id}/snapshots/{snapshot_id}/action

Administrator only. Force-deletes a share snapshot in any state.

Use the ``policy.json`` file to grant permissions for this action
to other roles.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - force_delete: force_delete
   - tenant_id: tenant_id
   - snapshot_id: snapshot_id

Request Example
---------------

.. literalinclude:: ../samples/manila-snapshot-actions-force-delete-request.json
   :language: javascript








