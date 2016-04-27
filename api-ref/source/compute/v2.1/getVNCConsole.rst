
Get VNC console (os-getVNCConsole action)
=========================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a VNC console for a server.

Specify the ``os-getVNCConsole`` action in the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-getVNCConsole: os-getVNCConsole
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/getVNCConsole-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/servers-action/getVNCConsole-create-response.json
   :language: javascript



