
Show bandwidth limit rule details
=================================

.. rest_method::  GET /v2.0/qos/policies/{policy_id}/bandwidth_limit_rules/{rule_id}

Shows details for a bandwidth limit rule for a QoS policy.


Normal response codes: 200
Error response codes:500,401,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - rule_id: rule_id
   - policy_id: policy_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - bandwidth_limit_rule: bandwidth_limit_rule
   - max_kbps: max_kbps
   - id: id
   - max_burst_kbps: max_burst_kbps
   - policy_id: policy_id




Response Example
----------------

.. literalinclude:: ../samples/qos/bandwidth_limit_rule-show-response.json
   :language: javascript






