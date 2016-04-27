
Reset consistency group snapshot state
======================================

.. rest_method::  POST /v2/{tenant_id}/cgsnapshots/{cgsnapshot_id}/action

Administrator only. Explicitly updates the state of a consistency group snapshot.

Administrators can use the ``policy.json`` file to permit other
roles to complete this action.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - tenant_id: tenant_id
   - cgsnapshot_id: cgsnapshot_id

Request Example
---------------

.. literalinclude:: ../samples/manila-cg-snapshot-reset-state-request.json
   :language: javascript








