
Reset share instance state
==========================

.. rest_method::  POST /v2/{tenant_id}/share_instances/{share_instance_id}/action

Administrator only. Explicitly updates the state of a share instance.

Use the ``policy.json`` file to grant permissions for this action
to other roles.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - tenant_id: tenant_id
   - share_instance_id: share_instance_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-instance-actions-reset-state-request.json
   :language: javascript








