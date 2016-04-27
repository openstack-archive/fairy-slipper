
Remove listener
===============

.. rest_method::  DELETE /v2.0/lbaas/listeners/{listener_id}

Removes a listener.

This operation removes a listener and its associated configuration
from the tenant account. The API immediately purges any and all
configuration data. You cannot recover it.

You cannot delete a listener if the load balancer to which it is
attached does not have an ``ACTIVE`` provisioning status.

Example: Delete a listener

Error response codes:204,400,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml














