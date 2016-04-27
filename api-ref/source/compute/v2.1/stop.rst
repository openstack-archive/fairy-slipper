
Stop server (os-stop action)
============================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Stops a running server and changes its status to ``SHUTOFF``.

Specify the ``os-stop`` action in the request body.

Preconditions

- The server status must be ``ACTIVE`` or ``ERROR``.

- If the server is locked, you must have administrator privileges to
  stop the server.

Asynchronous Postconditions

- After you successfully stop a server, its status changes to
  ``SHUTOFF``. The server instance data appears only on the compute
  node that Compute service manages.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-stop: os-stop
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/stop-request.json
   :language: javascript








