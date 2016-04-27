
Add bare metal node
===================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes

Adds a bare metal node to a server.

Preconditions

- You can add a bare metal node to a server with an ``ACTIVE``,
  ``PAUSED``, ``SHUTOFF``, ``VERIFY_RESIZE``, or ``SOFT_DELETED``
  status.

- You can add a bare metal node to a server with a status that is
  not locked.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/os-baremetal-nodes/baremetal-node-create-with-address-request.json
   :language: javascript
















