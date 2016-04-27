
Start server (os-start action)
==============================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Starts a stopped server and changes its status to ``ACTIVE``.

Specify the ``os-start`` action in the request body.

Preconditions

- The server status must be ``SHUTOFF``.

- If the server is locked, you must have administrator privileges to
  start the server.

Asynchronous Postconditions

- After you successfully start a server, its status changes to
  ``ACTIVE``. The server appears on the compute node that the
  Compute service manages.

Troubleshooting

- If the server status does not change to ``ACTIVE``, the start
  operation failed. Ensure that you meet the preconditions and run
  the request again. If the request fails again, investigate
  whether another operation is running that causes a race
  condition.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-start: os-start
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/start-request.json
   :language: javascript








