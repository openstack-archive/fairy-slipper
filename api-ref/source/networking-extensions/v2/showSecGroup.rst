
Show security group
===================

.. rest_method::  GET /v2.0/security-groups/{security_group_id}

Shows details for a security group.

The response contains the description, name, UUID, and security
group rules that are associated with the security group and tenant.


Normal response codes: 200
Error response codes:404,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - security_group_id: security_group_id
   - verbose: verbose
   - fields: fields



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




Response Example
----------------

.. literalinclude:: ../samples/security-groups/security-group-show-response.json
   :language: javascript





