
Show VLAN-transparent network details
=====================================

.. rest_method::  GET /v2.0/networks/{network_id}

Shows details for a VLAN-transparent network.


Normal response codes: 200
Error response codes:404,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - network_id: network_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - router:external: router:external
   - subnets: subnets
   - network: network
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - mtu: mtu
   - shared: shared
   - vlan_transparent: vlan_transparent
   - port_security_enabled: port_security_enabled
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/networks/network-vlan-transparent-show-response.json
   :language: javascript





