
Add (associate) fixed IP (addFixedIp action)
============================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Adds a fixed IP address to a server instance, which associates that address with the server. The fixed IP address is retrieved from the network that you specify in the request.

Specify the ``addFixedIp`` action and the network ID in the request
body.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - addFixedIp: addFixedIp
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/multinic-add-fixed-ip-request.json
   :language: javascript
















