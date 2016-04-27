
List bandwidth limit rules for QoS policy
=========================================

.. rest_method::  GET /v2.0/qos/policies/{policy_id}/bandwidth_limit_rules

Lists all bandwidth limit rules for a QoS policy.

The list might be empty.


Normal response codes: 200
Error response codes:500,401,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - policy_id: policy_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - max_kbps: max_kbps
   - bandwidth_limit_rules: bandwidth_limit_rules
   - id: id
   - max_burst_kbps: max_burst_kbps
   - policy_id: policy_id




Response Example
----------------

.. literalinclude:: ../samples/qos/bandwidth_limit_rules-list-response.json
   :language: javascript






