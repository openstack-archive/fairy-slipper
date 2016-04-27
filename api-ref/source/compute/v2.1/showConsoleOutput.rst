
Show console output (os-getConsoleOutput action)
================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Shows console output for a server instance.

Specify the ``os-getConsoleOutput`` action in the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-getConsoleOutput: os-getConsoleOutput
   - length: length
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/os-getConsoleOutput-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/servers-action/os-getConsoleOutput-create-response.json
   :language: javascript



