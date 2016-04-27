
Associate health monitor with pool
==================================

.. rest_method::  POST /v2.0/lb/pools/{pool_id}/health_monitors

Associates a health monitor with a pool.

Error response codes:201,400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - id: id
   - health_monitor: health_monitor
   - pool_id: pool_id

Request Example
---------------

.. literalinclude:: ../samples/lbaas/healthmonitor-associate-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - health_monitor: health_monitor










