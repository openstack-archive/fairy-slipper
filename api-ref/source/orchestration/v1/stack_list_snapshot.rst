
List snapshots
==============

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/snapshots

Lists snapshots for a stack.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - name: name
   - status_reason: status_reason
   - creation_time: creation_time
   - snapshots: snapshots
   - data: data
   - id: id




Response Example
----------------

.. literalinclude:: samples/stack-snapshots-list-response.json
   :language: javascript



