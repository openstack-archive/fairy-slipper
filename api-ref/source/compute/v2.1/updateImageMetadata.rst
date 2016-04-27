
Update image metadata items
===========================

.. rest_method::  POST /v2.1/{tenant_id}/images/{image_id}/metadata

Updates metadata items, by key, for an image.

Replaces items that match keys. Does not modify items not in the
request.


Normal response codes: 200
Error response codes:415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - image_id: image_id

Request Example
---------------

.. literalinclude:: ../samples/images/image-metadata-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - previous: previous
   - next: next




Response Example
----------------

.. literalinclude:: ../samples/images/image-metadata-create-response.json
   :language: javascript











