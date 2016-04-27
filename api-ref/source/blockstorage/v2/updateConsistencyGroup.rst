
Update consistency group
========================

.. rest_method::  PUT /v2/{tenant_id}/consistencygroups/{consistencygroup_id}/update

Updates a consistency group.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - remove_volumes: remove_volumes
   - description: description
   - add_volumes: add_volumes
   - name: name
   - tenant_id: tenant_id
   - consistencygroup_id: consistencygroup_id

Request Example
---------------

.. literalinclude:: ../samples/consistencygroups/consistency-group-update-request.json
   :language: javascript








