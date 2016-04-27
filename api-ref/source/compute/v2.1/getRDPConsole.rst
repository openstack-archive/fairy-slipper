
Get RDP console (os-getRDPConsole action)
=========================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets an `RDP <https://technet.microsoft.com/en-us/windowsserver/ee236407>`_ console for a server.

Specify the ``os-getRDPConsole`` action in the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-getRDPConsole: os-getRDPConsole
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/getRDPConsole-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/servers-action/getRDPConsole-create-response.json
   :language: javascript



