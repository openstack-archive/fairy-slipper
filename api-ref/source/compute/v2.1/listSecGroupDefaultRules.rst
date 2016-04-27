
List default security group rules
=================================

.. rest_method::  GET /v2.1/{tenant_id}/os-security-group-default-rules

Lists default security group rules.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



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

.. literalinclude:: ../samples/os-security-group-default-rules/security-group-default-rules-list-response.json
   :language: javascript









