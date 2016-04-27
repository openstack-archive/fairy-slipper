
Set image metadata for volume
=============================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Sets the image metadata for a volume. Specify the ``os-set_image_metadata`` action in the request body.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-set_image_metadata: os-set_image_metadata
   - metadata: metadata
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-image-metadata-set-request.json
   :language: javascript








