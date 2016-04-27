
List QoS policies
=================

.. rest_method::  GET /v2.0/qos/policies

Lists all QoS policies that are associated with your tenant account.

The list might be empty.


Normal response codes: 200
Error response codes:500,401,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - max_kbps: max_kbps
   - bandwidth_limit_rules: bandwidth_limit_rules
   - name: name
   - tenant_id: tenant_id
   - policies: policies
   - shared: shared
   - policy_id: policy_id
   - id: id
   - max_burst_kbps: max_burst_kbps
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/qos/policies-list-response.json
   :language: javascript






