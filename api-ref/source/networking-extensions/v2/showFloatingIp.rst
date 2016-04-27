
Show floating IP details
========================

.. rest_method::  GET /v2.0/floatingips/{floatingip_id}

Shows details for a floating IP.

Use the ``fields`` query parameter to control which fields are
returned in the response body. For information, see `Filtering and
Column Selection <http://specs.openstack.org/openstack /neutron-
specs/specs/api/networking_general_api_information.html #filtering-
and-column-                 selection>`_.

This example request shows details for a floating IP in JSON
format. This example also filters the result by the
``fixed_ip_address`` and ``floating_ip_address`` fields.

::

   GET /v2.0/floatingips/{floatingip_id}?fields=fixed_ip_address
   &
   fields=floating_ip_address
   Accept: application/json


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - floatingip_id: floatingip_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - router_id: router_id
   - status: status
   - floatingip: floatingip
   - tenant_id: tenant_id
   - floating_network_id: floating_network_id
   - fixed_ip_address: fixed_ip_address
   - floating_ip_address: floating_ip_address
   - port_id: port_id
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/routers/floatingip-show-response.json
   :language: javascript






