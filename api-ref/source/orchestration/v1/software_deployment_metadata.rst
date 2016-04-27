
Show server configuration metadata
==================================

.. rest_method::  GET /v1/{tenant_id}/software_deployments/metadata/{server_id}

Shows the deployment configuration metadata for a server.

Use the ``group`` property to specify the configuration hook to
which the pass the metadata item.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - server_id: server_id
   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: samples/deployment-metadata-response.json
   :language: javascript



