
Create security group
=====================

.. rest_method::  POST /v2.0/security-groups

Creates an OpenStack Networking security group.

This operation creates a security group with default security group
rules for the IPv4 and IPv6 ether types.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - security_group: security_group
   - tenant_id: tenant_id
   - description: description
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/security-groups/security-group-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - remote_group_id: remote_group_id
   - direction: direction
   - protocol: protocol
   - description: description
   - ethertype: ethertype
   - port_range_max: port_range_max
   - security_group_rules: security_group_rules
   - security_group_id: security_group_id
   - tenant_id: tenant_id
   - port_range_min: port_range_min
   - remote_ip_prefix: remote_ip_prefix
   - security_group: security_group
   - id: id
   - name: name







