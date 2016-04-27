
Clear admin password
====================

.. rest_method::  DELETE /v2.1/{tenant_id}/servers/{server_id}/os-server-password

Clears the encrypted administrative password for a server, which removes it from the metadata server.

This action does not actually change the instance server password.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id







