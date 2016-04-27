
List image members
==================

.. rest_method::  GET /v2/images/{image_id}/members

(Since Image API v2.1) Lists the tenants that share this image.

If a user who shares this image makes this call, the member list
contains only information for that user.

If a user who does not share this image makes this call, the call
returns the HTTP ``404`` response code.

Preconditions

- The image must exist.

- You must be the owner or a member of the image.


Normal response codes: 200
Error response codes:404,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - image_id: image_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - created_at: created_at
   - updated_at: updated_at
   - members: members
   - schema: schema




Response Example
----------------

.. literalinclude:: ../samples/image-members-list-response.json
   :language: javascript




