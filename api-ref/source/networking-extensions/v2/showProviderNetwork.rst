
Show network details
====================

.. rest_method::  GET /v2.0/networks/{network_id}

Shows details for a network.


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
   - availability_zone_hints: availability_zone_hints
   - availability_zones: availability_zones
   - name: name
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
   - network: network




Response Example
----------------

.. literalinclude:: ../samples/networks/network-show-response.json
   :language: javascript





