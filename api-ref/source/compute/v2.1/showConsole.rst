
Show console details
====================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/consoles/{console_id}

Shows details for a console for a server instance.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id
   - console_id: console_id






Response Example
----------------

.. literalinclude:: ../samples/os-consoles/consoles-list-response.json
   :language: javascript



