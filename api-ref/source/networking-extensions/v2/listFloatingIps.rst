
List floating IPs
=================

.. rest_method::  GET /v2.0/floatingips

Lists floating IPs that are accessible to the tenant who submits the request.

Default policy settings return only those floating IPs that are
owned by the tenant who submits the request, unless an admin user
submits the request.

This example request lists floating IPs in JSON format:

::

   GET /v2.0/floatingips
   Accept: application/json

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

   - router_id: router_id
   - status: status
   - tenant_id: tenant_id
   - floating_network_id: floating_network_id
   - fixed_ip_address: fixed_ip_address
   - floating_ip_address: floating_ip_address
   - port_id: port_id
   - id: id
   - floatingips: floatingips




Response Example
----------------

.. literalinclude:: ../samples/routers/floating-ips-list-response.json
   :language: javascript




