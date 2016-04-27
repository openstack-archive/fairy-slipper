
Create default security group rule
==================================

.. rest_method::  POST /v2.1/{tenant_id}/os-security-group-default-rules

Creates a default security group rule.

If you specify a source port (``from_port``) or destination port
(``to_port``) value, you must specify an IP protocol
(``ip_protocol``) value. Otherwise, the operation returns the ``Bad
Request (400)`` response code.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - to_port: to_port
   - cidr: cidr
   - from_port: from_port
   - id: id
   - ip_protocol: ip_protocol
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-security-group-default-rules/security-group-default-rule-create-request.json
   :language: javascript




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

.. literalinclude:: ../samples/os-security-group-default-rules/security-group-default-rule-create-response.json
   :language: javascript









