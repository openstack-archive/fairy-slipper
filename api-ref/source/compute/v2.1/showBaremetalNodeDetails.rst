
Show bare metal node details
============================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes/{node_id}

Shows details for a bare metal node.

Preconditions

- The bare metal node must be associated with the server.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id
   - node_id: node_id















