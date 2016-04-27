
Update firewall
===============

.. rest_method::  PUT /v2.0/fw/firewalls/{firewall_id}

Updates a firewall.

To update a service, the service status cannot be a ``PENDING_*``
status.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router_ids: router_ids
   - description: description
   - admin_state_up: admin_state_up
   - firewall: firewall
   - firewall_policy_id: firewall_policy_id
   - name: name
   - firewall_id: firewall_id

Request Example
---------------

.. literalinclude:: ../samples/firewalls/firewall-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - router_ids: router_ids
   - description: description
   - admin_state_up: admin_state_up
   - firewall: firewall
   - tenant_id: tenant_id
   - firewall_policy_id: firewall_policy_id
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/firewalls/firewall-update-response.json
   :language: javascript






