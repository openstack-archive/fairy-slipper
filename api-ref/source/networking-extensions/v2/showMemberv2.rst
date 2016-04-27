
Show pool member details
========================

.. rest_method::  GET /v2.0/lbaas/pools/{pool_id}/members/{member_id}

Shows details for a pool member.

This operation returns a member object identified by ``member_id``
that belongs to a pool object identified by ``pool_id``. If you are
not an administrative user and the pool or member object does not
belong to your tenant account, the service returns the HTTP
``Forbidden (403)`` response code.

If this operation succeeds, it returns a pool element.

Example: Show pool member details


Normal response codes: 200
Error response codes:404,403,500,401,413,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - status_description: status_description
   - weight: weight
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - pool_id: pool_id
   - member: member
   - address: address
   - protocol_port: protocol_port
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/lbaas/member-show-response.json
   :language: javascript










