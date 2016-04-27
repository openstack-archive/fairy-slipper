
Update image member
===================

.. rest_method::  PUT /v2/images/{image_id}/members/{member_id}

(Since Image API v2.1) Sets the status for an image member.

Preconditions

- The images must exist.

- You must be a member of the image.

Synchronous Postconditions

- If you update the member status to ``accepted`` and have the
  correct permissions, you see the image in list images responses.

- With correct permissions, you can make API calls to see the
  updated member status of the image.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - image_id: image_id
   - member_id: member_id

Request Example
---------------

.. literalinclude:: ../samples/image-member-update-request.json
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

.. literalinclude:: ../samples/image-member-update-response.json
   :language: javascript



