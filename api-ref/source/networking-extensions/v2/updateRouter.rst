
Update router
=============

.. rest_method::  PUT /v2.0/routers/{router_id}

Updates a logical router.

You can update the name, administrative state, and the external
gateway. For more information about how to set the external gateway
for a router, see the create router operation. This operation does
not enable the update of router interfaces. To update a router, use
the add router interface and remove router interface operations.

This example updates the external gateway information for a router:

::

   PUT /v2.0/routers/{router_id} Accept: application/json


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - external_gateway_info: external_gateway_info
   - enable_snat: enable_snat
   - name: name
   - admin_state_up: admin_state_up
   - router: router
   - external_fixed_ips: external_fixed_ips
   - router_id: router_id

Request Example
---------------

.. literalinclude:: ../samples/routers/router-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - external_gateway_info: external_gateway_info
   - status: status
   - availability_zone_hints: availability_zone_hints
   - availability_zones: availability_zones
   - name: name
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - distributed: distributed
   - enable_snat: enable_snat
   - routes: routes
   - router: router
   - ha: ha
   - id: id
   - external_fixed_ips: external_fixed_ips




Response Example
----------------

.. literalinclude:: ../samples/routers/router-update-response.json
   :language: javascript






