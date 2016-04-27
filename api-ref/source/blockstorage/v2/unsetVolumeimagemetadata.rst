
Remove image metadata from volume
=================================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Removes image metadata, by key, from a volume. Specify the ``os-unset_image_metadata`` action in the request body and the ``key`` for the metadata key and value pair that you want to remove.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-unset_image_metadata: os-unset_image_metadata
   - key: key
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-image-metadata-unset-request.json
   :language: javascript








