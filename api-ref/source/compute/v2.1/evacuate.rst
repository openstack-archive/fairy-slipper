
Evacuate server (evacuate action)
=================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Evacuates a server from a failed host to a new one.

Specify the ``evacuate`` action in the request body.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - host: host
   - evacuate: evacuate
   - adminPass: adminPass
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/evacuate-request.json
   :language: javascript








