
List security group rules
=========================

.. rest_method::  GET /v2.0/security-group-rules

Lists a summary of all OpenStack Networking security group rules that the tenant can access.

The list provides the UUID for each security group rule.


Normal response codes: 200
Error response codes:401,


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
   - security_group_rules: security_group_rules
   - security_group_id: security_group_id
   - tenant_id: tenant_id
   - port_range_min: port_range_min
   - remote_ip_prefix: remote_ip_prefix
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/security-groups/security-group-rules-list-response.json
   :language: javascript




