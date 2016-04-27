
Update pool member
==================

.. rest_method::  PUT /v2.0/lbaas/pools/{pool_id}/members/{member_id}

Updates attributes for a pool member.

Upon successful validation of the request, the service returns the
HTTP ``OK (200)`` response code.

Note: You cannot update the member UUID, ``tenant_id``,
``address``, ``protocol_port``, and ``subnet_id`` attributes. If
you attempt to update any of these attributes, the service returns
the HTTP ``Immutable (422)`` response code.

Note: You cannot update a member if the attached load balancer does
not have an ``ACTIVE`` provisioning status.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - member: member
   - pool_id: pool_id
   - weight: weight
   - admin_state_up: admin_state_up

Request Example
---------------

.. literalinclude:: ../samples/lbaas/member-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/lbaas/member-update-response.json
   :language: javascript








