
Show server action details
==========================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-instance-actions/{request_id}

Shows details for a server action.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id
   - request_id: request_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-instance-actions/instance-action-show-response.json
   :language: javascript



