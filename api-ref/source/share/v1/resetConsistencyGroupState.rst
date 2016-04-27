
Reset consistency group state
=============================

.. rest_method::  POST /v2/{tenant_id}/consistency-groups/{consistency_group_id}/action

Administrator only. Explicitly updates the state of a consistency group.

Use the ``policy.json`` file to grant permissions for this action
to other roles.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - tenant_id: tenant_id
   - consistency_group_id: consistency_group_id

Request Example
---------------

.. literalinclude:: ../samples/manila-consistency-group-reset-state-request.json
   :language: javascript








