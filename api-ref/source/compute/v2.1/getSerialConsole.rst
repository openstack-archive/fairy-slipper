
Get serial console (os-getSerialConsole action)
===============================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a serial console for a server.

Specify the ``os-getSerialConsole`` action in the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-getSerialConsole: os-getSerialConsole
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/getSerialConsole-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/servers-action/getSerialConsole-create-response.json
   :language: javascript



