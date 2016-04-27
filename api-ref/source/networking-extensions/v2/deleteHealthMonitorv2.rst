
Remove health monitor
=====================

.. rest_method::  DELETE /v2.0/lbaas/health_monitors/{health_monitor_id}

Removes a health monitor and its associated configuration from the tenant account.

The API immediately purges any and all configuration data. You
cannot recover it.

You cannot delete a health monitor if the attached load balancer
does not have an ``ACTIVE`` provisioning status.

Example: Delete a health monitor

Error response codes:204,400,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml














