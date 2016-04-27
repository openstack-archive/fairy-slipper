
Create share
============

.. rest_method::  POST /v2/{tenant_id}/shares

Creates a share.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - display_name: display_name
   - description: description
   - share_type: share_type
   - availability_zone: availability_zone
   - share_proto: share_proto
   - display_description: display_description
   - name: name
   - consistency_group_id: consistency_group_id
   - share_network_id: share_network_id
   - snapshot_id: snapshot_id
   - is_public: is_public
   - size: size
   - volume_type: volume_type
   - metadata: metadata
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - share_type_name: share_type_name
   - links: links
   - availability_zone: availability_zone
   - share_network_id: share_network_id
   - export_locations: export_locations
   - share_server_id: share_server_id
   - snapshot_id: snapshot_id
   - id: id
   - size: size
   - display_name: display_name
   - share_type: share_type
   - export_location: export_location
   - display_description: display_description
   - consistency_group_id: consistency_group_id
   - project_id: project_id
   - metadata: metadata
   - status: status
   - description: description
   - host: host
   - is_public: is_public
   - task_state: task_state
   - snapshot_support: snapshot_support
   - name: name
   - has_replicas: has_replicas
   - replication_type: replication_type
   - created_at: created_at
   - share_proto: share_proto
   - volume_type: volume_type
   - source_cgsnapshot_member_id: source_cgsnapshot_member_id




Response Example
----------------

.. literalinclude:: ../samples/manila-share-create-response.json
   :language: javascript



