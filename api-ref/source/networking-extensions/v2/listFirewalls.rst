
List firewalls
==============

.. rest_method::  GET /v2.0/fw/firewalls

Lists all firewalls.

The list might be empty.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - router_ids: router_ids
   - description: description
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - firewall_policy_id: firewall_policy_id
   - firewalls: firewalls
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/firewalls/firewalls-list-response.json
   :language: javascript





