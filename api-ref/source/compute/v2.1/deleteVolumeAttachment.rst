
Detach volume
=============

.. rest_method::  DELETE /v2.1/{tenant_id}/servers/{server_id}/os-volume_attachments/{attachment_id}

Detaches a volume from a server.

Preconditions

- The volume must be attached to the server.

- You can detach a volume when the server status is ``ACTIVE``,
  ``PAUSED``, ``SHUTOFF``, ``VERIFY_RESIZE``, or ``SOFT_DELETED``.

- You can detach a volume when its status is ``in-use``.

- You can detach a volume from a server with a status that is not
  locked.

- You cannot detach a root device volume.

Asynchronous Postconditions

- After successfully detaching a volume, its status changes to
  ``available``.

- The detached volume is no longer visible on the server.

Troubleshooting

- If the volume status remains in ``in-use`` state, the request
  failed. Ensure that you meet the preconditions and run the
  request again. If the request fails again, investigate whether
  another operation is running that causes a race condition.

- If you attempt to detach a root device volume, this operation
  returns the ``Forbidden (403)`` response code.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id
   - attachment_id: attachment_id















