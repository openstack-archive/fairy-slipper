
List VPN services
=================

.. rest_method::  GET /v2.0/vpn/vpnservices

Lists all VPN services.

The list might be empty.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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
   - vpnservices: vpnservices
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/vpn/vpnservices-list-response.json
   :language: javascript





