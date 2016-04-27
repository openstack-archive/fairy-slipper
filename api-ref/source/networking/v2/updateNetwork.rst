
Update network
==============

.. rest_method::  PUT /v2.0/networks/{network_id}

Updates a network.


Normal response codes: 200
Error response codes:404,403,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router:external: router:external
   - network: network
   - admin_state_up: admin_state_up
   - shared: shared
   - port_security_enabled: port_security_enabled
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
   - availability_zone_hints: availability_zone_hints
   - availability_zones: availability_zones
   - name: name
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - mtu: mtu
   - subnets: subnets
   - shared: shared
   - id: id
   - network: network




Response Example
----------------

.. literalinclude:: ../samples/networks/network-update-response.json
   :language: javascript







