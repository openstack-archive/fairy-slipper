
Disassociate health monitor from pool
=====================================

.. rest_method::  DELETE /v2.0/lb/pools/{pool_id}/health_monitors/{health_monitor_id}

Disassociates a health monitor from a pool.

Error response codes:204,400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - health_monitor_id: health_monitor_id
   - pool_id: pool_id












