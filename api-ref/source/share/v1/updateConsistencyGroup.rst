
Update consistency group
========================

.. rest_method::  PUT /v2/{tenant_id}/consistency-groups/{consistency_group_id}

Updates a consistency group.

You can update only these attributes:

- ``name``, which changes the consistency group name.

- ``description``, which changes the consistency group description.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - name: name
   - tenant_id: tenant_id
   - consistency_group_id: consistency_group_id

Request Example
---------------

.. literalinclude:: ../samples/manila-consistency-group-update-request.json
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

.. literalinclude:: ../samples/manila-consistency-group-update-response.json
   :language: javascript



