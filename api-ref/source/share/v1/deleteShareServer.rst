
Delete share server
===================

.. rest_method::  DELETE /v2/{tenant_id}/share-servers/{share_server_id}

Deletes a share server.

An administrator can delete an active share server only if it
contains no dependent shares.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - share_server_id: share_server_id







