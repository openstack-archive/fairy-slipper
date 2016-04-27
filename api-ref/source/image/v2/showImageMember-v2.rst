
Show image member details
=========================

.. rest_method::  GET /v2/images/{image_id}/members/{member_id}

(Since Image API v2.2) Shows image member details.

Response body is a single image member entity.

Preconditions

- The image must exist.

- You must be the owner or a member of the image.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - image_id: image_id
   - member_id: member_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - created_at: created_at
   - updated_at: updated_at
   - image_id: image_id
   - member_id: member_id
   - schema: schema




Response Example
----------------

.. literalinclude:: ../samples/image-member-details-response.json
   :language: javascript



