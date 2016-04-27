
Remove load balancer
====================

.. rest_method::  DELETE /v2.0/lbaas/loadbalancers/{loadbalancer_id}

Removes a load balancer and its associated configuration from the tenant account.

The API immediately purges any and all configuration data. You
cannot recover it.

Example: Delete a load balancer

Error response codes:204,400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml













