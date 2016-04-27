
Show VPN service details
========================

.. rest_method::  GET /v2.0/vpn/vpnservices/{service_id}

Shows details for a VPN service.

If the user is not an administrative user and the VPN service
object does not belong to the tenant account for the user, the
operation returns the ``Forbidden (403)`` response code.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_id: service_id



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

.. literalinclude:: ../samples/vpn/vpnservice-show-response.json
   :language: javascript






