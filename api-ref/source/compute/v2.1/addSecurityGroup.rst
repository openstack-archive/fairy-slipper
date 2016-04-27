
Add security group to a server (addSecurityGroup action)
========================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Adds a security group to a server.

Specify the ``addSecurityGroup`` action in the request body.

Error response codes:202,415,405,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - addSecurityGroup: addSecurityGroup
   - name: name
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action-admin/addSecurityGroup-request.json
   :language: javascript














