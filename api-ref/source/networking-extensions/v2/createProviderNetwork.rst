
Create network
==============

.. rest_method::  POST /v2.0/networks

Creates a network.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router:external: router:external
   - network: network
   - provider:physical_network: provider:physical_network
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - provider:network_type: provider:network_type
   - shared: shared
   - port_security_enabled: port_security_enabled
   - provider:segmentation_id: provider:segmentation_id
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/networks/network-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - router:external: router:external
   - availability_zone_hints: availability_zone_hints
   - network: network
   - provider:physical_network: provider:physical_network
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - provider:segmentation_id: provider:segmentation_id
   - mtu: mtu
   - shared: shared
   - subnets: subnets
   - port_security_enabled: port_security_enabled
   - provider:network_type: provider:network_type
   - id: id
   - name: name







