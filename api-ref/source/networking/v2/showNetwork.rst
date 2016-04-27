
Show network details
====================

.. rest_method::  GET /v2.0/networks/{network_id}

Shows details for a network.

You can control which response parameters are returned by using the
fields query parameter. For information, see `Filtering and column
selection <http://specs.openstack.org/openstack/neutron-
specs/specs/api/networking_general_api_information.html#filtering-
and-column-selection>`_.

The response might show extension response parameters. For
information, see `Networks multiple provider extension (networks)
<http://developer.openstack.org/api-ref-
networking-v2-ext.html#showProviderNetwork>`_.


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
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - updated_at: updated_at
   - changed_at: changed_at
   - mtu: mtu
   - subnets: subnets
   - shared: shared
   - id: id
   - network: network




Response Example
----------------

.. literalinclude:: ../samples/networks/network-show-response.json
   :language: javascript





