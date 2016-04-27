
Delete interface from bare metal node
=====================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes/action

Deletes an interface from a bare metal node that is associated with a server.

Error response codes:415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/os-baremetal-nodes/baremetal-node-remove-interface-request.json
   :language: javascript















