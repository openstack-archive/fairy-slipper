
Show console authentication token
=================================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-console-auth-token

Shows the authentication token for a console for a server instance.

This feature is available for ``rdp-html5`` console type only.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id






Response Example
----------------

.. literalinclude:: ../samples/os-consoles/console-auth-show-response.json
   :language: javascript



