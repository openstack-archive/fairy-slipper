
Remove (disassociate) floating IP (removeFloatingIp action)
===========================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Removes, or disassociates, a floating IP address from a server.

The IP address is returned to the pool of IP addresses that is
available for all projects. When you remove a floating IP address
and that IP address is still associated with a running instance, it
is automatically disassociated from that instance.

Specify the ``removeFloatingIp`` action in the request body.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - removeFloatingIp: removeFloatingIp
   - address: address
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/removeFloatingIp-request.json
   :language: javascript
















