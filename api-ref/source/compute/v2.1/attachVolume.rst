
Attach volume to server
=======================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/os-volume_attachments

Attaches a volume to a server.

Preconditions

- You can attach a volume to a server with an ``ACTIVE``,
  ``PAUSED``, ``SHUTOFF``, ``VERIFY_RESIZE``, or ``SOFT_DELETED``
  status.

- You can attach a volume to a server with a status that is not
  locked.

- You can attach a volume with a ``available`` status.

- You can attach a volume when its volume type supports volume
  attaching.

Asynchronous Postconditions

- After successfully attaching a volume to a server, the volume
  status changes to ``in-use``.

- You can see the attached volume when you log in to the server.

Troubleshooting

- If the volume status remains in ``available`` state, the request
  failed. Ensure that you meet the preconditions and run the
  request again. If the request fails again, investigate the server
  and the volume status.


Normal response codes: 200
Error response codes:415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - device: device
   - volumeAttachment: volumeAttachment
   - volumeId: volumeId
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/os-volumes/attach-volume-to-server-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-volumes/attach-volume-to-server-response.json
   :language: javascript











