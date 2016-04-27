
Add tags to image
=================

.. rest_method::  POST /v1.1/{tenant_id}/images/{image_id}/tag

Adds tags to an image.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tags: tags
   - image_id: image_id

Request Example
---------------

.. literalinclude:: ../samples/image-registry/image-tags-add-request.json
   :language: javascript








