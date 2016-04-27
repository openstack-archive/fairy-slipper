
Create a load balancer health monitor
=====================================

.. rest_method::  POST /v2.0/lb/health_monitors

Creates a load balancer health monitor.

Error response codes:201,400,401,413,503,500,


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










