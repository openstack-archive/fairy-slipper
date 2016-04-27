
Create snapshot
===============

.. rest_method::  POST /v2/{tenant_id}/snapshots

Creates a volume snapshot, which is a point-in-time, complete copy of a volume. You can create a volume from a snapshot.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - snapshot: snapshot
   - volume_id: volume_id
   - force: force
   - description: description
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/snapshot-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - created_at: created_at
   - name: name
   - snapshot: snapshot
   - volume_id: volume_id
   - metadata: metadata
   - id: id
   - size: size





