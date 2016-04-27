
Add interface to router
=======================

.. rest_method::  PUT /v2.0/routers/{router_id}/add_router_interface

Adds an internal interface to a logical router.

Attaches a subnet to an internal router interface.

Specify the UUID of a subnet or port in the request body:

- Subnet UUID. The gateway IP address for the subnet is used to
  create the router interface.

- Port UUID. The IP address associated with the port is used to
  create the router interface.

When you specify an IPv6 subnet, this operation adds the subnet to
an existing internal port with same network UUID, on the router. If
a port with the same network UUID does not exist, this operation
creates a port on the router for that subnet.

The limitation of one IPv4 subnet per router port remains, though a
port can contain any number of IPv6 subnets that belong to the same
network UUID.

When you use the ``port-create`` command to add a port and then
call ``router-interface-add`` with this port UUID, this operation
adds the port to the router if the following conditions are met:

- The port has no more than one IPv4 subnet.

  The IPv6 subnets, if any, on the port do not have same network
  UUID as the network UUID of IPv6 subnets on any other ports.

If you specify both UUIDs, this operation returns the ``Bad Request
(400)`` response code.

If the port is already in use, this operation returns the
``Conflict (409)`` response code.

This operation returns a port UUID that is either:

- The same UUID that is passed in the request body.

- The UUID of a port that this operation creates to attach the
  subnet to the router.

After you run this operation, the operation sets:

- The device UUID of this port to the router UUID.

- The ``device_owner`` attribute to ``network:router_interface``.


Normal response codes: 200
Error response codes:404,409,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - subnet_id: subnet_id
   - port_id: port_id
   - router_id: router_id

Request Example
---------------

.. literalinclude:: ../samples/routers/router-add-interface-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - port_id: port_id
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/routers/router-add-interface-response.json
   :language: javascript







