
Add members to image
====================

.. rest_method::  PUT /v1/images/{image_id}/members/{owner_id}

Adds one or more members to an image.

If you omit the request body, this call adds the membership to the
image, leaves the existing memberships unmodified, and sets the
``can_share`` attribute to ``false`` for new memberships.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - can_share: can_share
   - image_id: image_id
   - owner_id: owner_id

Request Example
---------------

.. literalinclude:: ../samples/image-members-add-request.json
   :language: javascript








