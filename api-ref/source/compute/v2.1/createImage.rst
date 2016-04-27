
Create image (createImage action)
=================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Creates an image from a server.

Specify the ``createImage`` action in the request body.

After you make this request, you typically must keep polling the
status of the created image to determine whether the request
succeeded.

If the operation succeeds, the created image has a status of
``active`` and the server status returns to the original status.
You can also see the new image in the image back end that OpenStack
Image service manages.

Preconditions

- The server must exist.

- You can only create a new image from the server when its status is
  ``ACTIVE``, ``SHUTOFF``, ``PAUSED``, or ``SUSPENDED``.

- The connection to the Image service is valid.

Troubleshooting

- If the image status remains uploading or shows another error
  status, the request failed. Ensure you meet the preconditions and
  run the request again. If the request fails again, investigate
  the image back end.

- If the server status does not go back to an original server's
  status, the request failed. Ensure you meet the preconditions, or
  check if there is another operation that causes race conditions
  for the server, then run the request again. If the request fails
  again, investigate the compute back end or ask your cloud
  provider.

- If the request fails due to an error on OpenStack Compute service,
  the image is purged from the image store that OpenStack Image
  service manages. Ensure you meet the preconditions and run the
  request again. If the request fails again, investigate OpenStack
  Compute service or ask your cloud provider.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - createImage: createImage
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/createImage-request.json
   :language: javascript
















