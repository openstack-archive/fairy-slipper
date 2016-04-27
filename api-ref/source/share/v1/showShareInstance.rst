
Show share instance details
===========================

.. rest_method::  GET /v2/{tenant_id}/share_instances/{share_instance_id}

Shows details for a share instance.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - share_instance_id: share_instance_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - replica_state: replica_state
   - availability_zone: availability_zone
   - created_at: created_at
   - export_location: export_location
   - share_network_id: share_network_id
   - export_locations: export_locations
   - share_server_id: share_server_id
   - host: host
   - share_id: share_id
   - access_rules_status: access_rules_status
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/manila-share-show-instance-response.json
   :language: javascript



