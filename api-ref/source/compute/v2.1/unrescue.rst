
Unrescue server (unrescue action)
=================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Unrescues a server. Changes status to ``ACTIVE``.

Specify the ``unrescue`` action in the request body.

Preconditions

- The server must exist.

- You can only unrescue a server when its status is ``RESCUE``.

Asynchronous Postconditions

- After you successfully unrescue a server and make a ``GET
  /v2.1/​{tenant_id}​/servers/​{server_id}​`` request, its status
  changes to ``ACTIVE``.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - unrescue: unrescue
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/unrescue-request.json
   :language: javascript








