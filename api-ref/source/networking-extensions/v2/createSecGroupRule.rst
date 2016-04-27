
Create security group rule
==========================

.. rest_method::  POST /v2.0/security-group-rules

Creates an OpenStack Networking security group rule.

Error response codes:201,404,409,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - remote_group_id: remote_group_id
   - direction: direction
   - protocol: protocol
   - ethertype: ethertype
   - port_range_max: port_range_max
   - security_group_id: security_group_id
   - security_group_rule: security_group_rule
   - port_range_min: port_range_min
   - remote_ip_prefix: remote_ip_prefix

Request Example
---------------

.. literalinclude:: ../samples/security-groups/security-group-rule-create-request.json
   :language: javascript




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









