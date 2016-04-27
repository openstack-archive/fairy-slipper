
Delete metadata item
====================

.. rest_method::  DELETE /v2.1/{tenant_id}/servers/{server_id}/metadata/{key}

Deletes a metadata item, by key, from a server.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id
   - key: key







