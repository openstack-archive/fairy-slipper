
Reset networking on a server (resetNetwork action)
==================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Resets networking on a server.

Specify the ``resetNetwork`` action in the request body.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - resetNetwork: resetNetwork
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action-admin/resetNetwork-request.json
   :language: javascript








