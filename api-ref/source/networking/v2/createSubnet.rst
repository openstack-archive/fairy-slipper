
Create subnet
=============

.. rest_method::  POST /v2.0/subnets

Creates a subnet on a network.

OpenStack Networking does not try to derive the correct IP version
from the CIDR. If you do not specify the ``gateway_ip`` attribute,
OpenStack Networking allocates an address from the CIDR for the
gateway for the subnet.

To specify a subnet without a gateway, set the ``gateway_ip``
attribute to ``null`` in the request body. If you do not specify
the ``allocation_pools`` attribute, OpenStack Networking
automatically allocates pools for covering all IP addresses in the
CIDR, excluding the address reserved for the subnet gateway.
Otherwise, you can explicitly specify allocation pools as shown in
the following example.

When you specify both the ``allocation_pools`` and ``gateway_ip``
attributes, you must ensure that the gateway IP does not overlap
with the allocation pools; otherwise, the call returns the
``Conflict (409)`` response code.

A subnet can have one or more name servers and host routes. Hosts
in this subnet use the name servers. Devices with IP addresses from
this subnet, not including the local subnet route, use the host
routes.

Specify the ``ipv6_ra_mode`` and ``ipv6_address_mode`` attributes
to create subnets that support IPv6 configurations, such as
stateless address autoconfiguration (SLAAC), DHCPv6 stateful, and
DHCPv6 stateless configurations.

Error response codes:201,404,403,401,400,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/subnets/subnet-create-request.json
   :language: javascript













