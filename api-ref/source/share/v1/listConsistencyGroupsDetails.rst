
List consistency groups with details
====================================

.. rest_method::  GET /v2/{tenant_id}/consistency-groups/detail

Lists all consistency groups with details.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - source_cgsnapshot_id: source_cgsnapshot_id
   - consistency_group: consistency_group
   - created_at: created_at
   - share_network_id: share_network_id
   - host: host
   - link: link
   - project_id: project_id
   - share_types: share_types
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-consistency-groups-list-detailed-response.json
   :language: javascript



