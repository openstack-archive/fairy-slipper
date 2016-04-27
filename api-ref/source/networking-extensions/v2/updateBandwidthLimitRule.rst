
Update bandwidth limit rule
===========================

.. rest_method::  PUT /v2.0/qos/policies/{policy_id}/bandwidth_limit_rules/{rule_id}

Updates a bandwidth limit rule for a QoS policy.

If the request is valid, the service returns the ``Accepted (202)``
response code.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - bandwidth_limit_rule: bandwidth_limit_rule
   - max_kbps: max_kbps
   - max_burst_kbps: max_burst_kbps
   - policy_id: policy_id
   - rule_id: rule_id
   - policy_id: policy_id

Request Example
---------------

.. literalinclude:: ../samples/qos/bandwidth_limit_rule-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/qos/bandwidth_limit_rule-update-response.json
   :language: javascript








