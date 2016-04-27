
Insert rule into a firewall policy
==================================

.. rest_method::  PUT /v2.0/fw/firewall_policies/{firewall_policy_id}/insert_rule

Insert firewall rule into a policy.

A firewall_rule_id is inserted relative to the position of the
firewall_rule_id set in ``insert_before`` or ``insert_after``. If
``insert_before`` is set, ``insert_after`` is ignored. If both
``insert_before`` and ``insert_after`` are not set, the new
firewall_rule_id is inserted at the top of the policy.


Normal response codes: 200
Error response codes:404,409,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - insert_after: insert_after
   - firewall_rule_id: firewall_rule_id
   - insert_before: insert_before
   - firewall_policy_id: firewall_policy_id

Request Example
---------------

.. literalinclude:: ../samples/firewalls/firewall-policy-insert-rule-request.json
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

.. literalinclude:: ../samples/firewalls/firewall-policy-insert-rule-response.json
   :language: javascript







