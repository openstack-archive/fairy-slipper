
Delete server
=============

.. rest_method::  DELETE /v2.1/{tenant_id}/servers/{server_id}

Deletes a server.

Preconditions

- The server must exist.

- Anyone can delete a server when the status of the server is not
  locked and when the policy allows.

- If the server is locked, you must have administrator privileges to
  delete the server.

Asynchronous postconditions

- With correct permissions, you can see the server status as
  ``DELETED`` through API calls.

- The port attached to the server is deleted.

- The server does not appear in the list servers response.

- The server managed by OpenStack Compute is deleted on the compute
  node.

Troubleshooting

- If server status remains in ``deleting`` status or another error
  status, the request failed. Ensure that you meet the
  preconditions. Then, investigate the compute back end.

- The request returns the HTTP 409 response code when the server is
  locked even if you have correct permissions. Ensure that you meet
  the preconditions then investigate the server status.

- The server managed by OpenStack Compute is not deleted from the
  compute node.

Error response codes:204,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id













