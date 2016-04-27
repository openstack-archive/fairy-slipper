
Update consistency group snapshot
=================================

.. rest_method::  PUT /v2/{tenant_id}/cgsnapshots/{cgsnapshot_id}

Updates a consistency group snapshot.

You can update only these attributes:

- ``name``, which changes the consistency group snapshot name.

- ``description``, which changes the consistency group snapshot
  description.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - name: name
   - tenant_id: tenant_id
   - cgsnapshot_id: cgsnapshot_id

Request Example
---------------

.. literalinclude:: ../samples/manila-cg-snapshot-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - links: links
   - cgsnapshot: cgsnapshot
   - created_at: created_at
   - consistency_group_id: consistency_group_id
   - project_id: project_id
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-cg-snapshot-update-response.json
   :language: javascript



