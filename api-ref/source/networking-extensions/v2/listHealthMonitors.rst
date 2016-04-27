
List health monitors
====================

.. rest_method::  GET /v2.0/lb/health_monitors

Lists health monitors.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - health_monitors: health_monitors
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

.. literalinclude:: ../samples/lbaas/healthmonitors-list-response.json
   :language: javascript








