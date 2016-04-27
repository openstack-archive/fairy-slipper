
Remove pool
===========

.. rest_method::  DELETE /v2.0/lbaas/pools/{pool_id}

Removes a pool.

This operation removes a pool and its associated configuration from
the tenant account. The API immediately purges any and all
configuration data. You cannot recover it.

You cannot delete a pool if the load balancer to which it is
attached does not have an ``ACTIVE`` provisioning status.

Error response codes:204,400,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml














