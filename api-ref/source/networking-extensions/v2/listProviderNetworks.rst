
List networks
=============

.. rest_method::  GET /v2.0/networks

Lists networks that are accessible to the tenant who submits the request.


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
   - availability_zone_hints: availability_zone_hints
   - availability_zones: availability_zones
   - name: name
   - provider:physical_network: provider:physical_network
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - networks: networks
   - mtu: mtu
   - shared: shared
   - subnets: subnets
   - port_security_enabled: port_security_enabled
   - provider:network_type: provider:network_type
   - id: id
   - provider:segmentation_id: provider:segmentation_id




Response Example
----------------

.. literalinclude:: ../samples/networks/networks-list-response.json
   :language: javascript




