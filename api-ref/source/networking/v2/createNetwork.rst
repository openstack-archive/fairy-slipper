
Create network
==============

.. rest_method::  POST /v2.0/networks

Creates a network.

A request body is optional. An administrative user can specify
another tenant UUID, which is the tenant who owns the network, in
the request body.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


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
   - availability_zones: availability_zones
   - name: name
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - mtu: mtu
   - subnets: subnets
   - shared: shared
   - id: id
   - network: network







