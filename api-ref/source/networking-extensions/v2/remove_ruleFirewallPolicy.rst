
Remove rule from firewall policy
================================

.. rest_method::  PUT /v2.0/fw/firewall_policies/{firewall_policy_id}/remove_rule

Remove firewall rule from a policy.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - firewall_rule_id: firewall_rule_id
   - firewall_policy_id: firewall_policy_id

Request Example
---------------

.. literalinclude:: ../samples/firewalls/firewall-policy-remove-rule-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - firewall_rules: firewall_rules
   - tenant_id: tenant_id
   - firewall_list: firewall_list
   - audited: audited
   - shared: shared
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/firewalls/firewall-policy-remove-rule-response.json
   :language: javascript






