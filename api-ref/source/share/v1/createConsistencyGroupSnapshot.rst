
Create consistency group snapshot
=================================

.. rest_method::  POST /v2/{tenant_id}/cgsnapshots

Creates a consistency group snapshot.

You can create a consistency group snapshot for a consistency group
in ``available`` state only.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - consistency_group_id: consistency_group_id
   - description: description
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-cg-snapshot-create-request.json
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

.. literalinclude:: ../samples/manila-cg-snapshot-create-response.json
   :language: javascript



