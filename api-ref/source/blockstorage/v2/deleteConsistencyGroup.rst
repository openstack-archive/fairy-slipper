
Delete consistency group
========================

.. rest_method::  POST /v2/{tenant_id}/consistencygroups/{consistencygroup_id}/delete

Deletes a consistency group.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - force: force
   - tenant_id: tenant_id
   - consistencygroup_id: consistencygroup_id

Request Example
---------------

.. literalinclude:: ../samples/consistencygroups/consistency-group-delete-request.json
   :language: javascript








