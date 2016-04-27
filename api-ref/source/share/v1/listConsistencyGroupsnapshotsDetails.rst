
List consistency group snapshots with details
=============================================

.. rest_method::  GET /v2/{tenant_id}/cgsnapshots/detail

Lists all consistency group snapshots with details.


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
   - links: links
   - created_at: created_at
   - consistency_group_id: consistency_group_id
   - project_id: project_id
   - id: id
   - cgsnapshots: cgsnapshots
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-cg-snapshots-list-detailed-response.json
   :language: javascript



