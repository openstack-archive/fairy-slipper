
Create volume
=============

.. rest_method::  POST /v2/{tenant_id}/volumes

Creates a volume.

To create a bootable volume, include the UUID of the image from
which you want to create the volume in the ``imageRef`` attribute
in the request body.

Preconditions

- You must have enough volume storage quota remaining to create a
  volume of size requested.

Asynchronous Postconditions

- With correct permissions, you can see the volume status as
  ``available`` through API calls.

- With correct access, you can see the created volume in the storage
  system that OpenStack Block Storage manages.

Troubleshooting

- If volume status remains ``creating`` or shows another error
  status, the request failed. Ensure you meet the preconditions
  then investigate the storage back end.

- Volume is not created in the storage system that OpenStack Block
  Storage manages.

- The storage node needs enough free storage space to match the size
  of the volume creation request.

Error response codes:202,


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

   - migration_status: migration_status
   - attachments: attachments
   - links: links
   - availability_zone: availability_zone
   - encrypted: encrypted
   - updated_at: updated_at
   - replication_status: replication_status
   - snapshot_id: snapshot_id
   - id: id
   - size: size
   - user_id: user_id
   - metadata: metadata
   - status: status
   - description: description
   - multiattach: multiattach
   - source_volid: source_volid
   - volume: volume
   - consistencygroup_id: consistencygroup_id
   - name: name
   - bootable: bootable
   - created_at: created_at
   - volume_type: volume_type





