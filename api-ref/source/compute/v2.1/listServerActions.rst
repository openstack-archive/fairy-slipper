
List actions for server
=======================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-instance-actions

Lists actions for a server.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-instance-actions/instance-actions-list-response.json
   :language: javascript



