
Show consistency group snapshot details
=======================================

.. rest_method::  GET /v2/{tenant_id}/cgsnapshots/{cgsnapshot_id}

Shows details for a consistency group snapshot.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - cgsnapshot_id: cgsnapshot_id



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

.. literalinclude:: ../samples/manila-cg-snapshot-show-response.json
   :language: javascript



