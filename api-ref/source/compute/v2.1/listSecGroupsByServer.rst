
List security groups by server
==============================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-security-groups

Lists security groups for a server.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id






Response Example
----------------

.. literalinclude:: ../samples/os-security-groups/security-groups-list-response.json
   :language: javascript



