
Remove member from pool
=======================

.. rest_method::  DELETE /v2.0/lbaas/pools/{pool_id}/members/{member_id}

Removes a member from a pool and its associated configuration from the tenant account.

The API immediately purges any and all configuration data. You
cannot recover it.

You cannot delete a member if the attached load balancer does not
have an ``ACTIVE`` provisioning status.

Example: Remove a member from a pool

Error response codes:204,400,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml














