
Show default security group rule details
========================================

.. rest_method::  GET /v2.1/{tenant_id}/os-security-group-default-rules/{security_group_default_rule_id}

Shows details for a security group rule.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - security_group_default_rule_id: security_group_default_rule_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - from_port: from_port
   - ip_protocol: ip_protocol
   - to_port: to_port
   - ip_range: ip_range
   - cidr: cidr
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/os-security-group-default-rules/security-group-default-rule-show-response.json
   :language: javascript









