
Create server back up (createBackup action)
===========================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Creates a back up of a server.

Specify the ``createBackup`` action in the request body.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - createBackup: createBackup
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action-admin/createBackup-request.json
   :language: javascript








