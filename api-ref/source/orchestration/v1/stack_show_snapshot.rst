
Show snapshot
=============

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/snapshots/{snapshot_id}

Shows details for a snapshot.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id
   - snapshot_id: snapshot_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - name: name
   - status_reason: status_reason
   - creation_time: creation_time
   - snapshot: snapshot
   - template: template
   - project_id: project_id
   - data: data
   - id: id
   - resources: resources




Response Example
----------------

.. literalinclude:: samples/stack-show-snapshot-response.json
   :language: javascript



