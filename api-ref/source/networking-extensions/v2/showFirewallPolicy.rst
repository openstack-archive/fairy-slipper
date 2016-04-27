
Show firewall policy details
============================

.. rest_method::  GET /v2.0/fw/firewall_policies/{firewall_policy_id}

Shows details for a firewall policy.

If the user is not an administrative user and the firewall policy
object does not belong to the tenant account, this call returns the
``Forbidden (403)`` response code.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - firewall_policy_id: firewall_policy_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - firewall_policy: firewall_policy
   - name: name
   - firewall_rules: firewall_rules
   - tenant_id: tenant_id
   - audited: audited
   - shared: shared
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/firewalls/firewall-policy-show-response.json
   :language: javascript






