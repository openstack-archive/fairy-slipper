
Update VPN service
==================

.. rest_method::  PUT /v2.0/vpn/vpnservices/{service_id}

Updates a VPN service.

Updates the attributes of a VPN service. You cannot update a
service with a ``PENDING_*`` status.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - vpnservice: vpnservice
   - description: description
   - name: name
   - admin_state_up: admin_state_up
   - service_id: service_id

Request Example
---------------

.. literalinclude:: ../samples/vpn/vpnservice-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/vpn/vpnservice-update-response.json
   :language: javascript






