
Show server diagnostics
=======================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/diagnostics

Shows basic usage data for a server.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id






Response Example
----------------

.. literalinclude:: ../samples/diagnostics/server-diagnostics-show-response.json
   :language: javascript



