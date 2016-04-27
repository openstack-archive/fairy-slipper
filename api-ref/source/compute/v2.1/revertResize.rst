
Revert resized server (revertResize action)
===========================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Cancels and reverts a pending resize action for a server.

Specify the ``revertResize`` action in the request body.

After you make this request, you typically must keep polling the
server status to determine whether the request succeeded. A
successfully reverting resize operation shows a status of
``ACTIVE`` or ``SHUTOFF`` and a migration_status of ``reverted``.
You can also see the reverted server in the compute node that
OpenStack Compute manages.

Preconditions

- You can only confirm the resized server where the status is
  ``VERIFY_RESIZE`` and the vm_status is ``RESIZED``.

- If the server is locked, you must have administrator privileges to
  revert the resizing.

Troubleshooting

- If the server status remains ``RESIZED``, the request failed.
  Ensure you meet the preconditions and run the request again. If
  the request fails again, investigate the compute back end.

- The server is not reverted in the compute node that OpenStack
  Compute manages.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - revertResize: revertResize
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/revertResize-request.json
   :language: javascript
















