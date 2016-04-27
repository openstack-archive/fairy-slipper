
Create IPSec connection
=======================

.. rest_method::  POST /v2.0/vpn/ipsec-site-connections

Creates a site-to-site IPSec connection for a service.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - auth_mode: auth_mode
   - ikepolicy_id: ikepolicy_id
   - vpnservice_id: vpnservice_id
   - local_ep_group_id: local_ep_group_id
   - peer_address: peer_address
   - ipsec_site_connection: ipsec_site_connection
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

Request Example
---------------

.. literalinclude:: ../samples/vpn/ipsec-site-connection-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - auth_mode: auth_mode
   - ikepolicy_id: ikepolicy_id
   - vpnservice_id: vpnservice_id
   - local_ep_group_id: local_ep_group_id
   - peer_address: peer_address
   - id: id
   - ipsec_site_connection: ipsec_site_connection
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







