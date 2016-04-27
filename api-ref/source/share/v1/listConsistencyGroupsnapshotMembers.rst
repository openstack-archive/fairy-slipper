
Show consistency group snapshot member
======================================

.. rest_method::  GET /v2/{tenant_id}/cgsnapshots/{cgsnapshot_id}/members

Shows information about a consistency group snapshot member.


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

   - share_type_id: share_type_id
   - share_id: share_id
   - created_at: created_at
   - cgsnapshot_id: cgsnapshot_id
   - share_protocol: share_protocol
   - cgsnapshot_members: cgsnapshot_members
   - project_id: project_id
   - id: id
   - size: size




Response Example
----------------

.. literalinclude:: ../samples/manila-cg-snapshots-list-members-response.json
   :language: javascript



