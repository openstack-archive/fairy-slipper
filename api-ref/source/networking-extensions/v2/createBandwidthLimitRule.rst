
Create bandwidth limit rule
===========================

.. rest_method::  POST /v2.0/qos/policies/{policy_id}/bandwidth_limit_rules

Creates a bandwidth limit rule for a QoS policy.

Error response codes:201,404,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - bandwidth_limit_rule: bandwidth_limit_rule
   - max_kbps: max_kbps
   - max_burst_kbps: max_burst_kbps
   - policy_id: policy_id
   - policy_id: policy_id

Request Example
---------------

.. literalinclude:: ../samples/qos/bandwidth_limit_rule-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - bandwidth_limit_rule: bandwidth_limit_rule
   - max_kbps: max_kbps
   - id: id
   - max_burst_kbps: max_burst_kbps
   - policy_id: policy_id











