
Restore snapshot
================

.. rest_method::  POST /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/snapshots/{snapshot_id}/restore

Restores a stack snapshot.

You can restore only active stacks from a snapshot. You must
recreate deleted stacks.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id
   - snapshot_id: snapshot_id







