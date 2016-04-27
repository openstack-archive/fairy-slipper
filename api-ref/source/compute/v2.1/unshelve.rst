
Unshelve (restore) shelved server (unshelve action)
===================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Unshelves, or restores, a shelved server.

Specify the ``unshelve`` action in the request body.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Preconditions

- The server status must be ``SHELVED`` or ``SHELVED_OFFLOADED``.

- If the server is locked, you must have administrator privileges to
  unshelve the server.

Asynchronous Postconditions

- After you successfully shelve a server, its status changes to
  ``ACTIVE``. The server appears on the compute node.

- The shelved image is deleted from the list of images returned by
  an API call.

Troubleshooting

- If the server status does not change to ``ACTIVE``, the unshelve
  operation failed. Ensure that you meet the preconditions and run
  the request again. If the request fails again, investigate
  whether another operation is running that causes a race
  condition.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - unshelve: unshelve
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/unshelve-request.json
   :language: javascript








