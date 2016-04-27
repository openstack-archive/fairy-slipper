
Create health monitor
=====================

.. rest_method::  POST /v2.0/lbaas/health_monitors

Creates a health monitor.

This operation provisions a health monitor by using the
configuration that you define in the request object. After the API
validates the request and start the provisioning process, it
returns a response object. The object contains a unique identifier.

At a minimum, you must specify these health monitor attributes:

- ``tenant_id``. Admin only. Required to create a health monitor for
  another tenant.

- ``type``. The type of health monitor. A valid value is ``TCP``,
  ``HTTP``, or ``HTTPS``.

- ``delay``. The interval, in seconds, between health checks.

- ``timeout``. The time, in seconds, after which a health check
  times out.

- ``max_retries``. Number of failed health checks before marked as
  OFFLINE.

- ``pool_id``. The pool to monitor.

Some attributes receive default values if you omit them from the
request, and are only useful when you specify a health monitor type
of HTTP(S):

- ``http_method``. Default is ``GET``.

- ``url_path``. Default is ``/``.

- ``expected_codes``. The expected HTTP status codes to get from a
  successful health check. Default is ``200``.

- ``admin_state_up``. Default is ``true``.

If the API cannot fulfill the request due to insufficient data or
data that is not valid, it returns the ``Bad Request (400)``
response code with information about the nature of the failure in
the response body. Failures in the validation process are non-
recoverable and require that you correct the cause of the failure
and submit the request again.

You can configure all documented features of the health monitor at
creation time by specifying the additional elements or attributes
in the request.

Administrative users can specify a tenant ID that is different than
their own to create health monitors for other tenants.

To update a health monitor, the load balancer to which to attach
must have an ``ACTIVE`` provisioning status.

Error response codes:201,404,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - health_monitor: health_monitor
   - tenant_id: tenant_id
   - admin_state_up: admin_state_up
   - delay: delay
   - expected_codes: expected_codes
   - max_retries: max_retries
   - http_method: http_method
   - timeout: timeout
   - url_path: url_path
   - type: type

Request Example
---------------

.. literalinclude:: ../samples/lbaas/healthmonitor-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - health_monitor: health_monitor
   - tenant_id: tenant_id
   - admin_state_up: admin_state_up
   - delay: delay
   - expected_codes: expected_codes
   - max_retries: max_retries
   - http_method: http_method
   - timeout: timeout
   - pools: pools
   - url_path: url_path
   - type: type
   - id: id











