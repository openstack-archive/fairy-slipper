
Update network
==============

.. rest_method::  PUT /v2.0/networks/{network_id}

Updates a network.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router:external: router:external
   - availability_zone_hints: availability_zone_hints
   - availability_zones: availability_zones
   - network: network
   - provider:physical_network: provider:physical_network
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - provider:network_type: provider:network_type
   - shared: shared
   - port_security_enabled: port_security_enabled
   - provider:segmentation_id: provider:segmentation_id
   - name: name
   - network_id: network_id

Request Example
---------------

.. literalinclude:: ../samples/networks/network-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - router:external: router:external
   - subnets: subnets
   - network: network
   - provider:physical_network: provider:physical_network
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - provider:segmentation_id: provider:segmentation_id
   - mtu: mtu
   - shared: shared
   - port_security_enabled: port_security_enabled
   - provider:network_type: provider:network_type
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/networks/network-update-response.json
   :language: javascript






