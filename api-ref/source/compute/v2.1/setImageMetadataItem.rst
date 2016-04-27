
Create or update image metadata item
====================================

.. rest_method::  PUT /v2.1/{tenant_id}/images/{image_id}/metadata/{key}

Creates or updates a metadata item, by key, for an image.


Normal response codes: 200
Error response codes:415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - key: key
   - image_id: image_id

Request Example
---------------

.. literalinclude:: ../samples/images/image-metadata-item-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/images/image-metadata-item-update-response.json
   :language: javascript











