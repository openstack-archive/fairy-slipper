
Create consistency group from source
====================================

.. rest_method::  POST /v2/{tenant_id}/consistencygroups/create_from_src

Creates a consistency group from source.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - user_id: user_id
   - description: description
   - cgsnapshot_id: cgsnapshot_id
   - source_cgid: source_cgid
   - project_id: project_id
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/consistencygroups/consistency-group-create-from-src-request.json
   :language: javascript








