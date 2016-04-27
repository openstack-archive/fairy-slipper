
Show router details
===================

.. rest_method::  GET /v2.0/routers/{router_id}

Shows details for a router.

This example request shows details for a router in JSON format:

::

   GET /v2.0/routers/{router_id} Accept: application/json

Use the ``fields`` query parameter to control which fields are
returned in the response body. For information, see `Filtering and
Column Selection <http://specs.openstack.org/openstack/neutron-
specs/specs/api/networking_general_api_information.html#filtering-
and-column-selection>`_.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router_id: router_id



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

.. literalinclude:: ../samples/routers/router-show-response.json
   :language: javascript






