
Delete interface from router
============================

.. rest_method::  PUT /v2.0/routers/{router_id}/remove_router_interface

Deletes an internal interface from a logical router.

This operation deletes an internal router interface, which detaches
a subnet from the router. If this subnet UUID is the last subnet on
the port, this operation deletes the port itself. You must specify
either a subnet UUID or port UUID in the request body; the
operation uses this value to identify which router interface to
deletes.

You can also specify both a subnet UUID and port UUID. If you
specify both UUIDs, the subnet UUID must correspond to the subnet
UUID of the first IP address on the port. Otherwise, this operation
returns the ``Conflict (409)`` response code with information about
the affected router and interface.

If the router or the subnet and port do not exist or are not
visible to you, this operation returns the ``Not Found (404)``
response code. As a consequence of this operation, the operation
removes the port connecting the router with the subnet from the
subnet for the network.

This example deletes an interface from a router:

::

   PUT /v2.0/routers/{router_id}/remove_router_interface Accept: application/json


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

.. literalinclude:: ../samples/routers/router-remove-interface-request.json
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

.. literalinclude:: ../samples/routers/router-remove-interface-response.json
   :language: javascript







