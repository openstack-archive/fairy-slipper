
List networks with VLAN transparency attribute
==============================================

.. rest_method::  GET /v2.0/networks

Lists networks. The response shows the VLAN transparency attribute.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - router:external: router:external
   - subnets: subnets
   - name: name
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - mtu: mtu
   - vlan_transparent: vlan_transparent
   - shared: shared
   - id: id
   - port_security_enabled: port_security_enabled
   - networks: networks




Response Example
----------------

.. literalinclude:: ../samples/networks/networks-vlan-transparent-list-response.json
   :language: javascript




