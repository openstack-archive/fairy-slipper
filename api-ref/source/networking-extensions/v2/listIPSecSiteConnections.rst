
List IPSec connections
======================

.. rest_method::  GET /v2.0/vpn/ipsec-site-connections

Lists all IPSec connections.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - auth_mode: auth_mode
   - ikepolicy_id: ikepolicy_id
   - vpnservice_id: vpnservice_id
   - local_ep_group_id: local_ep_group_id
   - peer_address: peer_address
   - id: id
   - route_mode: route_mode
   - ipsecpolicy_id: ipsecpolicy_id
   - peer_id: peer_id
   - status: status
   - psk: psk
   - description: description
   - initiator: initiator
   - peer_cidrs: peer_cidrs
   - name: name
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - interval: interval
   - mtu: mtu
   - peer_ep_group_id: peer_ep_group_id
   - dpd: dpd
   - timeout: timeout
   - action: action




Response Example
----------------

.. literalinclude:: ../samples/vpn/ipsec-site-connections-list-response.json
   :language: javascript





