
Force detach volume
===================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Forces a volume to detach. Specify the ``os-force_detach`` action in the request body.

Rolls back an unsuccessful detach operation after you disconnect
the volume.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - connector: connector
   - attachment_id: attachment_id
   - os-force_detach: os-force_detach
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-force-detach-request.json
   :language: javascript








