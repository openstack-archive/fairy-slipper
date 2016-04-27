
Add member to pool
==================

.. rest_method::  POST /v2.0/lbaas/pools/{pool_id}/members

Adds a member to a pool.

This operation provisions a member and adds it to a pool by using
the configuration that you define in the request object. After the
API validates the request and starts the provisioning process, it
returns a response object, which contains a unique ID.

At a minimum, you must specify these pool attributes:

- ``tenant_id``. Admin only. Required to create a pool for another
  tenant.

- ``address``. The IP address of the member to receive traffic from
  the load balancer.

- ``protocol_port`` The port on which the member listens for
  traffic.

Some attributes receive default values if you omit them from the
request:

- ``admin_state_up``. Default is ``true``.

- ``weight``. Default is ``1``.

If you omit the ``subnet_id`` parameter, LBaaS uses the
``vip_subnet_id`` parameter value for the subnet UUID.

If the request fails due to incorrect data, the service returns the
HTTP ``Bad Request (400)`` response code with information about the
failure in the response body. Validation errors require that you
correct the error and submit the request again.

To configure all documented member features at creation time,
specify additional elements or attributes in the request.

Administrative users can specify a tenant ID that is different than
their own to create members for other tenants.

To update a member, the load balancer must have an ``ACTIVE``
provisioning status.

Error response codes:201,404,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - member: member
   - subnet_id: subnet_id
   - protocol_port: protocol_port
   - tenant_id: tenant_id
   - address: address

Request Example
---------------

.. literalinclude:: ../samples/lbaas/member-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - weight: weight
   - admin_state_up: admin_state_up
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - member: member
   - address: address
   - protocol_port: protocol_port
   - id: id











