
Create volume
=============

.. rest_method::  POST /v1/{tenant_id}/volumes

Creates a volume.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - size: size
   - description: description
   - imageRef: imageRef
   - multiattach: multiattach
   - availability_zone: availability_zone
   - source_volid: source_volid
   - name: name
   - volume: volume
   - consistencygroup_id: consistencygroup_id
   - volume_type: volume_type
   - snapshot_id: snapshot_id
   - scheduler_hints: scheduler_hints
   - source_replica: source_replica
   - metadata: metadata
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - imageRef: imageRef
   - multiattach: multiattach
   - created_at: created_at
   - availability_zone: availability_zone
   - source_volid: source_volid
   - name: name
   - volume: volume
   - volume_type: volume_type
   - snapshot_id: snapshot_id
   - size: size
   - metadata: metadata





