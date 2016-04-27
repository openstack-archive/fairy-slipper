
Show volume details
===================

.. rest_method::  GET /v2/{tenant_id}/volumes/{volume_id}

Shows details for a volume.

Preconditions

- The volume must exist.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - volume_id: volume_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - migration_status: migration_status
   - attachments: attachments
   - links: links
   - availability_zone: availability_zone
   - os-vol-host-attr:host: os-vol-host-attr:host
   - encrypted: encrypted
   - updated_at: updated_at
   - os-volume-replication:extended_status: os-volume-replication:extended_status
   - replication_status: replication_status
   - snapshot_id: snapshot_id
   - id: id
   - size: size
   - user_id: user_id
   - os-vol-tenant-attr:tenant_id: os-vol-tenant-attr:tenant_id
   - os-vol-mig-status-attr:migstat: os-vol-mig-status-attr:migstat
   - metadata: metadata
   - status: status
   - description: description
   - multiattach: multiattach
   - source_volid: source_volid
   - volume: volume
   - consistencygroup_id: consistencygroup_id
   - os-vol-mig-status-attr:name_id: os-vol-mig-status-attr:name_id
   - name: name
   - bootable: bootable
   - created_at: created_at
   - os-volume-replication:driver_data: os-volume-replication:driver_data
   - volume_type: volume_type




Response Example
----------------

.. literalinclude:: ../samples/volumes/volume-show-response.json
   :language: javascript



