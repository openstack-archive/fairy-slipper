
List volumes, with details
==========================

.. rest_method::  GET /v1/{tenant_id}/volumes/detail

Lists all volumes, with details.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



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
   - consistencygroup_id: consistencygroup_id
   - name: name
   - bootable: bootable
   - created_at: created_at
   - volume_type: volume_type
   - volumes: volumes




Response Example
----------------

.. literalinclude:: ../samples/volumes/volumes-list-response.json
   :language: javascript



