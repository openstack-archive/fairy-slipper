
Create listener
===============

.. rest_method::  POST /v2.0/lbaas/listeners

Creates a listener.

This operation provisions a new listener by using the configuration
that you define in the request object. After the request is
validated and the provisioning process begins, a response object is
returned. The object contains a unique identifier.

At a minimum, you must specify these listener attributes:

- ``tenant_id``. Admin only. Required to create a listener for
  another tenant.

- ``loadbalancer_id``. The load balancer on which to provision this
  listener. A tenant can only create listeners on load balancers
  that the policy authorizes. For example, her own load balancers.

- ``description``. The load balancer description.

- ``protocol``. The protocol for which the front end listens. Must
  be ``HTTP``, ``HTTPS``, ``TCP``, or ``TERMINATED_HTTPS``.

Some attributes receive default values if you omit them from the
request:

- ``protocol_port``. The port on which the front end listens. Must
  be an integer from 1 to 65535.

- ``default_tls_container_ref``. The reference to a container that
  holds TLS secrets. If you also specify ``sni_container_refs``,
  this container is the default. This parameter is required for the
  ``TERMINATED_HTTPS`` protocol.

- ``sni_container_refs``. A list of references to containers that
  hold TLS secrets for server name indication (SNI). This parameter
  is required for the ``TERMINATED_HTTPS`` protocol.

- ``admin_state_up``. Default is ``true``.

- ``name``. Default is an empty string.

- ``description``. Default is an empty string.

- ``connection_limit``. Default is ``-1``, which indicates an
  infinite limit.

If the API cannot fulfill the request due to insufficient data or
data that is not valid, the service returns the HTTP ``Bad Request
(400)`` response code with information about the failure in the
response body. Validation errors require that you correct the error
and submit the request again.

You can configure all documented features of the listener at
creation time by specifying the additional elements or attributes
in the request.

Administrative users can specify a tenant ID that is different than
their own to create listeners for other tenants.

To update a listener, the load balancer to which to attach must
have an ``ACTIVE`` provisioning status.

Error response codes:201,404,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - protocol_port: protocol_port
   - protocol: protocol
   - description: description
   - default_tls_container_ref: default_tls_container_ref
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - sni_container_refs: sni_container_refs
   - connection_limit: connection_limit
   - listener: listener
   - default_pool_id: default_pool_id
   - loadbalancer_id: loadbalancer_id
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/lbaas/listener-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - protocol_port: protocol_port
   - protocol: protocol
   - description: description
   - default_tls_container_ref: default_tls_container_ref
   - admin_state_up: admin_state_up
   - loadbalancers: loadbalancers
   - tenant_id: tenant_id
   - sni_container_refs: sni_container_refs
   - connection_limit: connection_limit
   - listener: listener
   - default_pool_id: default_pool_id
   - id: id
   - name: name











