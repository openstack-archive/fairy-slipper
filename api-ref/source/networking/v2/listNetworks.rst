
List networks
=============

.. rest_method::  GET /v2.0/networks

Lists networks to which the tenant has access.

Use the ``fields`` query parameter to filter the response. For
information, see `Filtering and Column Selection <https://wiki.open
stack.org/wiki/Neutron/APIv2-specification#Filtering_and_Column_Sel
ection>`_.

Use the ``tags``, ``tags-any``, ``not-tags``, ``not-tags-any``
query parameter to filter the response with tags. For information,
see `REST API Impact <http://specs.openstack.org/openstack/neutron-
specs/specs/mitaka/add-tags-to-core-resources.html#rest-api-
impact>`_.


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
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - networks: networks
   - mtu: mtu
   - subnets: subnets
   - shared: shared
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/networks/networks-list-response.json
   :language: javascript




