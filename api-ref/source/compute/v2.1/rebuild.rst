
Rebuild server (rebuild action)
===============================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Rebuilds a server.

Specify the ``rebuild`` action in the request body.

To rebuild the server with preservation of the ephemeral partition,
set the ``preserve_ephemeral`` parameter to ``true``.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - imageRef: imageRef
   - adminPass: adminPass
   - rebuild: rebuild
   - preserve_ephemeral: preserve_ephemeral
   - metadata: metadata
   - personality: personality
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/rebuild-preserve-ephemeral-request.json
   :language: javascript
















