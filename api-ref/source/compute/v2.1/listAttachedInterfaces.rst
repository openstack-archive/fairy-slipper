
List port interfaces
====================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-interface

Lists port interfaces that are attached to a server.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - fixed_ips: fixed_ips
   - port_state: port_state
   - mac_addr: mac_addr
   - interfaceAttachment: interfaceAttachment
   - port_id: port_id
   - net_id: net_id




Response Example
----------------

.. literalinclude:: ../samples/os-interface/port-interfaces-list-response.json
   :language: javascript









