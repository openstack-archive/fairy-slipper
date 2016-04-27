
Force-delete share instance
===========================

.. rest_method::  POST /v2/{tenant_id}/share_instances/{share_instance_id}/action

Administrator only. Force-deletes a share instance.

Use the ``policy.json`` file to grant permissions for this action
to other roles.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - force_delete: force_delete
   - tenant_id: tenant_id
   - share_instance_id: share_instance_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-instance-actions-force-delete-request.json
   :language: javascript








