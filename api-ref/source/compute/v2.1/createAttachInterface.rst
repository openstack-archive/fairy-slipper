
Create interface
================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/os-interface

Creates a port interface and uses it to attach a port to a server instance.


Normal response codes: 200
Error response codes:415,405,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - interfaceAttachment: interfaceAttachment
   - port_id: port_id
   - fixed_ips: fixed_ips
   - net_id: net_id
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/os-interface/port-interface-create-request.json
   :language: javascript




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

.. literalinclude:: ../samples/os-interface/port-interface-create-response.json
   :language: javascript









