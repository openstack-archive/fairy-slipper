
List shares with details
========================

.. rest_method::  GET /v2/{tenant_id}/shares/detail

Lists all shares, with details.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - is_public: is_public
   - tenant_id: tenant_id
   - all_tenants: all_tenants
   - name: name
   - status: status
   - share_server_id: share_server_id
   - metadata: metadata
   - extra_specs: extra_specs
   - share_type_id: share_type_id
   - limit: limit
   - offset: offset
   - sort_key: sort_key
   - sort_dir: sort_dir
   - snapshot_id: snapshot_id
   - host: host
   - share_network_id: share_network_id
   - project_id: project_id
   - consistency_group_id: consistency_group_id



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
   - share_type: share_type
   - export_location: export_location
   - consistency_group_id: consistency_group_id
   - project_id: project_id
   - metadata: metadata
   - status: status
   - description: description
   - host: host
   - access_rules_status: access_rules_status
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

.. literalinclude:: ../samples/manila-shares-list-detailed-response.json
   :language: javascript



