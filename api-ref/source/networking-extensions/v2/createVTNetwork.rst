
Create VLAN-transparent network
===============================

.. rest_method::  POST /v2.0/networks

Creates a VLAN-transparent network.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router:external: router:external
   - network: network
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - shared: shared
   - vlan_transparent: vlan_transparent
   - port_security_enabled: port_security_enabled
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/networks/network-vlan-transparent-create-request.json
   :language: javascript




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







