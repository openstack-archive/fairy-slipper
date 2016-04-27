
Create consistency group
========================

.. rest_method::  POST /v2/{tenant_id}/consistency-groups

Creates a consistency group.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - source_cgsnapshot_id: source_cgsnapshot_id
   - share_types: share_types
   - description: description
   - share_network_id: share_network_id
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-consistency-group-create-request.json
   :language: javascript




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

.. literalinclude:: ../samples/manila-consistency-group-create-response.json
   :language: javascript



