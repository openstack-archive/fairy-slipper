
Create load balancer
====================

.. rest_method::  POST /v2.0/lbaas/loadbalancers

Creates a load balancer.

This operation provisions a new load balancer by using the
configuration that you define in the request object. After the API
validates the request and starts the provisioning process, the API
returns a response object that contains a unique ID and the status
of provisioning the load balancer.

In the response, the load balancer provisioning status is
``ACTIVE``, ``PENDING_CREATE``, or ``ERROR``.

If the status is ``PENDING_CREATE``, issue GET
``/lbaas/loadbalancers/loadbalancer_id`` to view the progress of
the provisioning operation. When the load balancer status changes
to ``ACTIVE``, the load balancer is successfully provisioned and
operational for traffic handling.

If the API cannot fulfill the request due to insufficient data or
data that is not valid, the service returns the HTTP ``Bad Request
(400)`` response code with information about the failure in the
response body. Validation errors require that you correct the error
and submit the request again.

You can configure all documented features of the load balancer at
creation time by specifying the additional elements or attributes
in the request.

Administrative users can specify a tenant ID that is different than
their own to create load balancers for other tenants.

**Example: Create a load balancer**

- ``tenant_id``. Admin only. Required to create a load balancer for
  another tenant.

- ``vip_subnet_id``. The network on which to allocate the VIP
  address for the load balancer. A tenant can only create load
  balancer VIPs on networks that the policy authorizes, such as her
  own networks or shared or provider networks.

Some attributes receive default values if you omit them from the
request:

- ``admin_state_up``. Default is ``true``.

- ``name``. Default is an empty string.

- ``description``. Default is an empty string.

If the API cannot fulfill the request due to insufficient data or
data that is not valid, the service returns the HTTP ``Bad Request
(400)`` response code with information about the failure in the
response body. Validation errors require that you correct the error
and submit the request again.

You can configure all documented features of the load balancer at
creation time by specifying the additional elements or attributes
in the request.

Administrative users can specify a tenant ID that is different than
their own to create load balancers for other tenants.

If you own the subnet where you want to create the load balancer
VIP, you can specify a ``vip_address`` attribute. If you omit the
``vip_address`` attribute from the payload, the LBaaS service
allocates a VIP address from the subnet of the load balancer VIP.

An optional ``flavor`` attribute can be passed to enable dynamic
selection of an appropriate provider if configured by the operator.
The basic selection algorithm chooses the provider in the first
service profile currently associated with flavor.

You can also specify the ``provider`` attribute when you create a
load balancer. You can set this attribute to any service provider
with a ``LOADBALANCER`` service type. Setting both a flavor and a
provider will result in a conflict error.

Example: Create a load balancer

Error response codes:201,404,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - vip_address: vip_address
   - provider: provider
   - vip_subnet_id: vip_subnet_id
   - flavor: flavor
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/lbaas/loadbalancer-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - provisioning_status: provisioning_status
   - listeners: listeners
   - vip_address: vip_address
   - operating_status: operating_status
   - provider: provider
   - vip_subnet_id: vip_subnet_id
   - flavor: flavor
   - id: id
   - loadbalancer: loadbalancer
   - name: name











