
Shelf-offload (remove) server (shelveOffload action)
====================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Shelf-offloads, or removes, a shelved server.

Specify the ``shelveOffload`` action in the request body.

Data and resource associations are deleted. If an instance is no
longer needed, you can remove that instance from the hypervisor to
minimize resource usage.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Preconditions

- The server status must be ``SHELVED``.

- If the server is locked, you must have administrator privileges to
  shelve-offload the server.

Asynchronous Postconditions

- After you successfully shelve-offload a server, its status changes
  to ``SHELVED_OFFLOADED``. The server instance data appears on the
  compute node.

Troubleshooting

- If the server status does not change to ``SHELVED_OFFLOADED``, the
  shelve-offload operation failed. Ensure that you meet the
  preconditions and run the request again. If the request fails
  again, investigate whether another operation is running that
  causes a race condition.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - shelveOffload: shelveOffload
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/shelveOffload-request.json
   :language: javascript








