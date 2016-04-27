
Update load balancer
====================

.. rest_method::  PUT /v2.0/lbaas/loadbalancers/{loadbalancer_id}

Updates a load balancer.

If the request is valid, the service returns the ``Accepted (202)``
response code. To confirm the update, check that the load balancer
provisioning status is ``ACTIVE``. If the status is
``PENDING_UPDATE``, use a GET operation to poll the load balancer
object for changes.

This operation returns the updated load balancer object with the
``ACTIVE``, ``PENDING_UPDATE``, or ``ERROR`` provisioning status.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - description: description
   - loadbalancer: loadbalancer
   - admin_state_up: admin_state_up

Request Example
---------------

.. literalinclude:: ../samples/lbaas/loadbalancer-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - provisioning_status: provisioning_status
   - listeners: listeners
   - vip_address: vip_address
   - operating_status: operating_status
   - provider: provider
   - vip_subnet_id: vip_subnet_id
   - flavor: flavor
   - id: id
   - loadbalancer: loadbalancer
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/lbaas/loadbalancer-update-response.json
   :language: javascript








