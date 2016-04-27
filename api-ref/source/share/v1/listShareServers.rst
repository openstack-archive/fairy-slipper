
List share servers
==================

.. rest_method::  GET /v2/{tenant_id}/share-servers

Lists all share servers.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - updated_at: updated_at
   - share_network_id: share_network_id
   - host: host
   - share_network_name: share_network_name
   - project_id: project_id
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/manila-share-servers-list-response.json
   :language: javascript



