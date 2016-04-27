
Show details for a network with multiple segments
=================================================

.. rest_method::  GET /v2.0/networks/{network_id}

Shows details for a network with multiple segments.


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
   - provider:physical_network: provider:physical_network
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - segments: segments
   - provider:segmentation_id: provider:segmentation_id
   - mtu: mtu
   - shared: shared
   - port_security_enabled: port_security_enabled
   - provider:network_type: provider:network_type
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/networks/networks-multi-show-response.json
   :language: javascript





