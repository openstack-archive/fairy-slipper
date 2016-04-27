
Remove (disassociate) fixed IP (removeFixedIp action)
=====================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Removes, or disassociates, a fixed IP address from a server.

Specify the ``removeFixedIp`` action in the request body.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - removeFixedIp: removeFixedIp
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/multinic-remove-fixed-ip-request.json
   :language: javascript
















