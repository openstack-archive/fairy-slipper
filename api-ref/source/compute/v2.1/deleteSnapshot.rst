
Delete snapshot
===============

.. rest_method::  DELETE /v2.1/{tenant_id}/os-snapshots/{snapshot_id}

Deletes a snapshot from the account.

This operation is asynchronous. You must list snapshots repeatedly
to determine whether the snapshot was deleted.

Error response codes:202,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - snapshot_id: snapshot_id













