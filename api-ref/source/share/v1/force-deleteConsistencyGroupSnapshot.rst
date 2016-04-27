
Force-delete consistency group snapshot
=======================================

.. rest_method::  POST /v2/{tenant_id}/cgsnapshots/{cgsnapshot_id}/action

Administrator only. Force-deletes a consistency group snapshot.

Use the ``policy.json`` file to grant permissions for this action
to other roles.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - force_delete: force_delete
   - tenant_id: tenant_id
   - cgsnapshot_id: cgsnapshot_id

Request Example
---------------

.. literalinclude:: ../samples/manila-cg-snapshot-force-delete-request.json
   :language: javascript








