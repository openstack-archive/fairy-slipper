
Reboot server (reboot action)
=============================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Reboots a server.

Specify the ``reboot`` action in the request body.

Error response codes:202,415,405,404,403,401,400,422,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - reboot: reboot
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/reboot-request.json
   :language: javascript

















