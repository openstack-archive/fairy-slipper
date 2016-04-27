
Confirm resized server (confirmResize action)
=============================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Confirms a pending resize action for a server.

Specify the ``confirmResize`` action in the request body.

After you make this request, you typically must keep polling the
server status to determine whether the request succeeded. A
successfully confirming resize operation shows a status of
``ACTIVE`` or ``SHUTOFF`` and a migration_status of ``confirmed``.
You can also see the resized server in the compute node that
OpenStack Compute manages.

Preconditions

- You can only confirm the resized server where the status is
  ``VERIFY_RESIZED``, the vm_status is ``RESIZED``, and the
  migration_status is ``finished`` or ``confirming``.

- If the server is locked, you must have administrator privileges to
  confirm the server.

Troubleshooting

- If the server status remains ``RESIZED``, the request failed.
  Ensure you meet the preconditions and run the request again. If
  the request fails again, investigate the compute back end or ask
  your cloud provider.

Error response codes:204,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - confirmResize: confirmResize
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/confirmResize-request.json
   :language: javascript
















