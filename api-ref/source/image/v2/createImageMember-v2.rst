
Create image member
===================

.. rest_method::  POST /v2/images/{image_id}/members

(Since Image API v2.1) Adds a tenant ID as an image member.

This call accepts either the ``member_id`` or ``member`` attribute
in the request body. If you specify both attributes, the API uses
the ``member_id`` value and ignores the ``member`` value. Use of
the ``member`` attribute is supported but deprecated. Use of the
``member_id`` attribute is preferred.

Preconditions

- The images must exist.

- You can add a member to a private image.

- You must be the owner of the image.

Synchronous Postconditions

- With correct permissions, you can see the member status of the
  image as ``pending`` through API calls.

Troubleshooting

- Even if you have correct permissions, if the ``visibility``
  attribute is set to ``public``, the request returns the HTTP
  ``403`` response code. Ensure that you meet the preconditions and
  run the request again. If the request fails again, review your
  API request.

- If the member is already a member for the image, the service
  returns the ``Conflict (409)`` response code. If you meant to
  specify a different member, run the request again.


Normal response codes: 200
Error response codes:403,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - member: member
   - member_id: member_id
   - image_id: image_id

Request Example
---------------

.. literalinclude:: ../samples/image-member-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - created_at: created_at
   - schema: schema
   - updated_at: updated_at
   - member_id: member_id




Response Example
----------------

.. literalinclude:: ../samples/image-member-create-response.json
   :language: javascript





