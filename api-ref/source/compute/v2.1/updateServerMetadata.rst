
Update metadata items
=====================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/metadata

Updates one or more metadata items for a server.

Replaces metadata items that match keys. Does not modify items that
are not in the request.

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

Request Example
---------------

.. literalinclude:: ../samples/metadata/server-metadata-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/metadata/server-metadata-list-response.json
   :language: javascript



