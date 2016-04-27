
Create or update metadata item
==============================

.. rest_method::  PUT /v2.1/{tenant_id}/servers/{server_id}/metadata/{key}

Creates or replaces a metadata item, by key, for a server.

Creates a metadata item that does not already exist in the server.
Removes and completely replaces a metadata item that already exists
in the server with the metadata item in the request.

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
   - key: key

Request Example
---------------

.. literalinclude:: ../samples/metadata/server-metadata-item-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/metadata/server-metadata-item-show-response.json
   :language: javascript



