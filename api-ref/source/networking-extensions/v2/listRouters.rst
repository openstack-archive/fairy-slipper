
List routers
============

.. rest_method::  GET /v2.0/routers

Lists logical routers that the tenant who submits the request can access.

Default policy settings return only those routers that the tenant
who submits the request owns, unless an administrative user submits
the request.

This example request lists routers in JSON format:

::

   GET /v2.0/routers Accept: application/json

Use the ``fields`` query parameter to control which fields are
returned in the response body. Additionally, you can filter results
by using query string parameters. For information, see `Filtering
and Column Selection <https://wiki.openstack.org/wiki/Neutron/APIv2
-specification#Filtering_and_Column_Selection>`_.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - external_gateway_info: external_gateway_info
   - status: status
   - availability_zone_hints: availability_zone_hints
   - availability_zones: availability_zones
   - name: name
   - admin_state_up: admin_state_up
   - routers: routers
   - distributed: distributed
   - enable_snat: enable_snat
   - tenant_id: tenant_id
   - routes: routes
   - ha: ha
   - id: id
   - external_fixed_ips: external_fixed_ips




Response Example
----------------

.. literalinclude:: ../samples/routers/routers-list-response.json
   :language: javascript




