
Create security group rule
==========================

.. rest_method::  POST /v2.1/{tenant_id}/os-security-group-rules

Creates a rule for a security group.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - from_port: from_port
   - ip_protocol: ip_protocol
   - to_port: to_port
   - security_group_rule: security_group_rule
   - parent_group_id: parent_group_id
   - cidr: cidr
   - group_id: group_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-security-group-rules/security-group-rule-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - from_port: from_port
   - group: group
   - ip_protocol: ip_protocol
   - to_port: to_port
   - security_group_rule: security_group_rule
   - parent_group_id: parent_group_id
   - ip_range: ip_range
   - cidr: cidr
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/os-security-group-rules/security-group-rule-create-response.json
   :language: javascript



