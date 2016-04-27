
Reset volume statuses
=====================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Resets the status, attach status, and migration status for a volume. Specify the ``os-reset_status`` action in the request body.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - migration_status: migration_status
   - os-reset_status: os-reset_status
   - attach_status: attach_status
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-status-reset-request.json
   :language: javascript








