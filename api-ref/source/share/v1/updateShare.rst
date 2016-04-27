
Update share
============

.. rest_method::  PUT /v2/{tenant_id}/shares/{share_id}

Updates a share.

You can update these attributes:

- ``display_name``, which also changes the ``name`` of the share.

- ``display_description``, which also changes the ``description`` of
  the share.

- ``is_public``. Changes the level of visibility.

If you try to update other attributes, they retain their previous
values.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - is_public: is_public
   - display_name: display_name
   - display_description: display_description
   - share_id: share_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-update-request.json
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

.. literalinclude:: ../samples/manila-share-update-response.json
   :language: javascript



