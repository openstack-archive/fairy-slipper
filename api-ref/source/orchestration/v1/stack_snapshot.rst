
Snapshot stack
==============

.. rest_method::  POST /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/snapshots

Takes a snapshot of all resources in a stack. All snapshots are deleted when the stack is deleted.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id

Request Example
---------------

.. literalinclude:: samples/stack-snapshot-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - name: name
   - status_reason: status_reason
   - creation_time: creation_time
   - data: data
   - id: id




Response Example
----------------

.. literalinclude:: samples/stack-snapshot-response.json
   :language: javascript



