
Update health monitor
=====================

.. rest_method::  PUT /v2.0/lbaas/health_monitors/{health_monitor_id}

Updates a health monitor.

Upon successful validation of the request, the service returns the
HTTP ``Accepted (202)`` response code.

Note: The health monitor UUID, ``tenant_id``, ``pool_id``, and type
are immutable attributes and cannot be updated. If you specify an
unsupported attribute, the service returns the HTTP ``Immutable
(422)`` response code.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - health_monitor: health_monitor
   - admin_state_up: admin_state_up
   - delay: delay
   - expected_codes: expected_codes
   - max_retries: max_retries
   - http_method: http_method
   - timeout: timeout
   - url_path: url_path

Request Example
---------------

.. literalinclude:: ../samples/lbaas/healthmonitor-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/lbaas/healthmonitor-update-response.json
   :language: javascript








