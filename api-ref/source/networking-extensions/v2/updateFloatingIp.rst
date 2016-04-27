
Update floating IP
==================

.. rest_method::  PUT /v2.0/floatingips/{floatingip_id}

Updates a floating IP and its association with an internal port.

The association process is the same as the process for the create
floating IP operation.

To disassociate a floating IP from a port, set the ``port_id``
attribute to null or omit it from the request body.

This example updates a floating IP:

::

   PUT /v2.0/floatingips/{floatingip_id} Accept: application/json

Depending on the request body that you submit, this request
associates a port with or disassociates a port from a floating IP.


Normal response codes: 200
Error response codes:404,409,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - port_id: port_id
   - floatingip: floatingip
   - floatingip_id: floatingip_id

Request Example
---------------

.. literalinclude:: ../samples/routers/floatingip-disassociate-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/routers/floatingip-disassociate-response.json
   :language: javascript







