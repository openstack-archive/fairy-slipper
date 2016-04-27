
Reset share snapshot state
==========================

.. rest_method::  POST /v2/{tenant_id}/snapshots/{snapshot_id}/action

Administrator only. Explicitly updates the state of a share snapshot.

Use the ``policy.json`` file to grant permissions for this action
to other roles.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - tenant_id: tenant_id
   - snapshot_id: snapshot_id

Request Example
---------------

.. literalinclude:: ../samples/manila-snapshot-actions-reset-state-request.json
   :language: javascript








