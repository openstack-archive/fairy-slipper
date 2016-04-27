
Create firewall
===============

.. rest_method::  POST /v2.0/fw/firewalls

Creates a firewall.

The firewall must be associated with a firewall policy.

If ``admin_state_up`` is ``false``, the firewall would block all
traffic.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router_ids: router_ids
   - description: description
   - admin_state_up: admin_state_up
   - firewall: firewall
   - firewall_policy_id: firewall_policy_id
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/firewalls/firewall-create-request.json
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







