
Create VPN service
==================

.. rest_method::  POST /v2.0/vpn/vpnservices

Creates a VPN service.

The service is associated with a router. After you create the
service, it can contain multiple VPN connections.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router_id: router_id
   - description: description
   - admin_state_up: admin_state_up
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - vpnservice: vpnservice
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/vpn/vpnservice-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - router_id: router_id
   - status: status
   - name: name
   - external_v6_ip: external_v6_ip
   - admin_state_up: admin_state_up
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - external_v4_ip: external_v4_ip
   - vpnservice: vpnservice
   - id: id
   - description: description







