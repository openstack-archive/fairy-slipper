
List pool members
=================

.. rest_method::  GET /v2.0/lbaas/pools/{pool_id}/members

Lists members of a pool.

Lists all members that are associated with a pool that is
associated with your tenant account. The list of members includes
only members that belong to the pool object identified by
``pool_id``.

The list might be empty.

Example: List pool members


Normal response codes: 200
Error response codes:500,401,503,


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
   - members: members
   - address: address
   - protocol_port: protocol_port
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/lbaas/pool-members-list-response.json
   :language: javascript






