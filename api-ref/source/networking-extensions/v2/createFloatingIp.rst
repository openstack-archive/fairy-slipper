
Create floating IP
==================

.. rest_method::  POST /v2.0/floatingips

Creates a floating IP, and, if you specify port information, associates the floating IP with an internal port.

To associate the floating IP with an internal port, specify the
port UUID attribute in the request body. If you do not specify a
port UUID in the request, you can issue a PUT request instead of a
POST request.

Default policy settings enable only administrative users to set
floating IP addresses and some non-administrative users might
require a floating IP address. If you do not specify a floating IP
address in the request, the operation automatically allocates one.

By default, this operation associates the floating IP address with
a single fixed IP address that is configured on an OpenStack
Networking port. If a port has multiple IP addresses, you must
specify the ``fixed_ip_address`` attribute in the request body to
associate a fixed IP address with the floating IP address.

You can create floating IPs on only external networks. When you
create a floating IP, you must specify the UUID of the network on
which you want to create the floating IP. Alternatively, you can
create a floating IP on a subnet in the external network, based on
the costs and quality of that subnet.

You must configure an IP address with the internal OpenStack
Networking port that is associated with the floating IP address.

Error codes:

- ``400`` The operation returns this error code for one of these
  reasons:

  - The network is not external, such as ``router:external=False``.

  - The internal OpenStack Networking port is not associated with the
    floating IP address.

  - The requested floating IP address does not fall in the subnet
    range for the external network.

  - The fixed IP address is not valid.

- ``401`` The operation is not authorized.

- ``404`` The port UUID is not valid.

- ``409`` The operation returns this error code for one of these
  reasons:

  - The requested floating IP address is already in use.

  - The internal OpenStack Networking port and fixed IP address are
    already associated with another floating IP.

Error response codes:201,404,409,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - floatingip: floatingip
   - tenant_id: tenant_id
   - floating_network_id: floating_network_id
   - fixed_ip_address: fixed_ip_address
   - floating_ip_address: floating_ip_address
   - port_id: port_id

Request Example
---------------

.. literalinclude:: ../samples/routers/floatingip-create-request.json
   :language: javascript




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









