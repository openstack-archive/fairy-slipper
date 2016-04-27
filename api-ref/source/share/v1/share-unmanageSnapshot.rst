
Unmanage share snapshot
=======================

.. rest_method::  POST /v2/{tenant_id}/snapshots/{snapshot_id}/action

(Since API v2.12) Configures Shared File Systems to stop managing a share snapshot.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - unmanage: unmanage
   - tenant_id: tenant_id
   - snapshot_id: snapshot_id

Request Example
---------------

.. literalinclude:: ../samples/manila-snapshot-actions-unmanage-request.json
   :language: javascript








