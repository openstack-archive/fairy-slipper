
Create or replace metadata items
================================

.. rest_method::  PUT /v2.1/{tenant_id}/servers/{server_id}/metadata

Creates or replaces one or more metadata items for a server.

Creates any metadata items that do not already exist in the server.
Removes and completely replaces any metadata items that already
exist in the server with the metadata items in the request.

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



