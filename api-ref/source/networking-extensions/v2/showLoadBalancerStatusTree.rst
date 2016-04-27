
Show load balancer status tree
==============================

.. rest_method::  GET /v2.0/lbaas/loadbalancers/{loadbalancer_id}/statuses

Shows the status tree for a load balancer.

This operation returns a status tree for a load balancer object, by
load balancer ID. If you are not an administrative user and the
load balancer object does not belong to the tenant account, the API
returns the ``Forbidden (403)`` response code.

If the operation succeeds, the returned element is a status tree
that contains the load balancer and all provisioning and operating
statuses for its children.


Normal response codes: 200
Error response codes:403,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - provisioning_status: provisioning_status
   - listeners: listeners
   - healthmonitor: healthmonitor
   - members: members
   - pools: pools
   - id: id
   - operating_status: operating_status




Response Example
----------------

.. literalinclude:: ../samples/lbaas/loadbalancer-status-tree.json
   :language: javascript








