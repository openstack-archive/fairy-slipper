
Remove security group from a server (removeSecurityGroup action)
================================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Removes a security group from a server.

Specify the ``removeSecurityGroup`` action in the request body.

Error response codes:202,415,405,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - removeSecurityGroup: removeSecurityGroup
   - name: name
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action-admin/removeSecurityGroup-request.json
   :language: javascript














