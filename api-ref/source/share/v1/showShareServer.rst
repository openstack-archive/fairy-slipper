
Show share server details
=========================

.. rest_method::  GET /v2/{tenant_id}/share-servers/{share_server_id}

Shows details for a share server.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - share_server_id: share_server_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - backend_details: backend_details
   - created_at: created_at
   - updated_at: updated_at
   - share_network_id: share_network_id
   - host: host
   - share_network_name: share_network_name
   - project_id: project_id
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/manila-share-server-show-response.json
   :language: javascript



