
List health monitors
====================

.. rest_method::  GET /v2.0/lbaas/health_monitors

Lists health monitors.

This operation lists all health monitors that are associated with
your tenant account.

This operation returns a list, which might be empty.


Normal response codes: 200
Error response codes:500,401,503,


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






