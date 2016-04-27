
Show security group rule
========================

.. rest_method::  GET /v2.0/security-group-rules/{security-group-rules-id}

Shows detailed information for a security group rule.

The response body contains the following information about the
security group rule:


Normal response codes: 200
Error response codes:404,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - remote_group_id: remote_group_id
   - direction: direction
   - protocol: protocol
   - ethertype: ethertype
   - port_range_max: port_range_max
   - security_group_id: security_group_id
   - security_group_rule: security_group_rule
   - tenant_id: tenant_id
   - port_range_min: port_range_min
   - remote_ip_prefix: remote_ip_prefix
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/security-groups/security-group-rule-show-response.json
   :language: javascript





