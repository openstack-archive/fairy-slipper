
Show firewall details
=====================

.. rest_method::  GET /v2.0/fw/firewalls/{firewall_id}

Shows details for a firewall.

If the user is not an administrative user and the firewall object
does not belong to the tenant account, this call returns the
``Forbidden (403)`` response code.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - firewall_id: firewall_id



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

.. literalinclude:: ../samples/firewalls/firewall-show-response.json
   :language: javascript






