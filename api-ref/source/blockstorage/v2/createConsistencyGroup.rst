
Create consistency group
========================

.. rest_method::  POST /v2/{tenant_id}/consistencygroups

Creates a consistency group.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - user_id: user_id
   - description: description
   - availability_zone: availability_zone
   - volume_types: volume_types
   - project_id: project_id
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/consistencygroups/consistency-group-create-request.json
   :language: javascript








