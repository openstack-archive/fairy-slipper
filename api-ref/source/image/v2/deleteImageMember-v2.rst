
Delete image member
===================

.. rest_method::  DELETE /v2/images/{image_id}/members/{member_id}

(Since Image API v2.1) Deletes a tenant ID from the member list of an image.

Preconditions

- The image must exist.

- You must be the owner of the image.

Synchronous Postconditions

- The API removes the member from the image members.

Troubleshooting

- Even if you have correct permissions, if you are not the owner of
  the image or you specify an incorrect image ID or member ID, the
  call returns the HTTP ``403`` or ``404`` response code. Ensure
  that you meet the preconditions and run the request again. If the
  request fails again, review your API request URI.

Error response codes:404,403,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - image_id: image_id
   - member_id: member_id









