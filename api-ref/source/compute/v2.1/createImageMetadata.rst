
Create or replace image metadata
================================

.. rest_method::  PUT /v2.1/{tenant_id}/images/{image_id}/metadata

Creates or replaces metadata for an image.

Replaces items that match keys. If you omit a key that already
exists, this key retains its value.


Normal response codes: 200
Error response codes:415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - image_id: image_id

Request Example
---------------

.. literalinclude:: ../samples/images/image-metadata-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - previous: previous
   - next: next




Response Example
----------------

.. literalinclude:: ../samples/images/image-metadata-update-response.json
   :language: javascript











