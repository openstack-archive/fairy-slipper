
Show server password
====================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-server-password

Shows the administrative password for a server.

This operation calls the metadata service to query metadata
information and does not read password information from the server
itself.

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

.. literalinclude:: ../samples/os-server-password/password-show-response.json
   :language: javascript



