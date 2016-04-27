
Create pool
===========

.. rest_method::  POST /v2.0/lbaas/pools

Creates a pool.

This operation provisions a pool by using the configuration that
you define in the request object. After the API validates the
request and starts the provisioning process, the API returns a
response object, which contains a unique ID.

At a minimum, you must specify these pool attributes:

- ``tenant_id``. Admin only. Required to create a pool for another
  tenant.

- ``protocol``. The protocol for which this pool and its members
  listen. A valid value is ``TCP``, ``HTTP``, or ``HTTPS``.

- ``lb_algorithm``. The load-balancer algorithm, such as
  ``ROUND_ROBIN``, ``LEAST_CONNECTIONS``, and ``SOURCE_IP``, that
  distributes traffic to the pool members. The load-balancer
  provider must support this algorithm.

- ``listener_id``. The UUID of the listener in which this pool
  becomes the default pool. Each listener has only one default
  pool.

Some attributes receive default values if you omit them from the
request:

- ``admin_state_up``. Default is ``true``.

- ``name``. Default is an empty string.

- ``description``. Default is an empty string.

- ``session_persistence``. Default is an empty dictionary.

If the API cannot fulfill the request due to insufficient data or
data that is not valid, the service returns the HTTP ``Bad Request
(400)`` response code with information about the failure in the
response body. Validation errors require that you correct the error
and submit the request again.

Users can configure all documented features at creation time by
providing the additional elements or attributes in the request.

Administrative users can specify a tenant ID that is different than
their own to create pools for other tenants.

To update a pool, the load balancer to which to attach must have an
``ACTIVE`` provisioning status.

Error response codes:201,404,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - lb_algorithm: lb_algorithm
   - protocol: protocol
   - description: description
   - admin_state_up: admin_state_up
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - listener_id: listener_id
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/lbaas/pool-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - lb_algorithm: lb_algorithm
   - status: status
   - protocol: protocol
   - description: description
   - vip_id: vip_id
   - admin_state_up: admin_state_up
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - session_persistence: session_persistence
   - healthmonitor_id: healthmonitor_id
   - health_monitors_status: health_monitors_status
   - members: members
   - id: id
   - pool: pool
   - name: name











