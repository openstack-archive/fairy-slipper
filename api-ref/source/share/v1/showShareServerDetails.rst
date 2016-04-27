
Show share server details
=========================

.. rest_method::  GET /v2/{tenant_id}/share-servers/{share_server_id}/detail

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

   - backend_details: backend_details




Response Example
----------------

.. literalinclude:: ../samples/manila-share-server-show-details-response.json
   :language: javascript



