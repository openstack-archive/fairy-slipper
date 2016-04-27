
Show health monitor details
===========================

.. rest_method::  GET /v2.0/lbaas/health_monitors/{health_monitor_id}

Shows details for a health monitor.

This operation returns a health monitor object, by health monitor
ID. If you are not an administrative user and the health monitor
object does not belong to your tenant account, the service returns
the HTTP ``Forbidden (403)`` response code.

Example: Show health monitor details


Normal response codes: 200
Error response codes:404,403,500,401,413,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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

.. literalinclude:: ../samples/lbaas/healthmonitor-show-response.json
   :language: javascript










