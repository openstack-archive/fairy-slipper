
Show QoS policy details
=======================

.. rest_method::  GET /v2.0/qos/policies/{policy_id}

Shows details for a QoS policy.


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
   - name: name
   - tenant_id: tenant_id
   - policy: policy
   - shared: shared
   - policy_id: policy_id
   - id: id
   - max_burst_kbps: max_burst_kbps
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/qos/policy-show-response.json
   :language: javascript






