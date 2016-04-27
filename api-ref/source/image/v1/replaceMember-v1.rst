
Replace member
==============

.. rest_method::  PUT /v1/images/{image_id}/members

Replaces a membership list for an image.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - memberships: memberships
   - can_share: can_share
   - image_id: image_id

Request Example
---------------

.. literalinclude:: ../samples/image-members-add-request.json
   :language: javascript








