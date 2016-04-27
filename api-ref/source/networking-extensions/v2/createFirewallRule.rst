
Create firewall rule
====================

.. rest_method::  POST /v2.0/fw/firewall_rules

Creates a firewall rule.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - firewall_rule: firewall_rule
   - description: description
   - tenant_id: tenant_id
   - enabled: enabled
   - ip_version: ip_version
   - destination_ip_address: destination_ip_address
   - source_port: source_port
   - shared: shared
   - action: action
   - protocol: protocol
   - destination_port: destination_port
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/firewalls/firewall-rule-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - firewall_rule: firewall_rule
   - description: description
   - source_ip_address: source_ip_address
   - tenant_id: tenant_id
   - enabled: enabled
   - protocol: protocol
   - source_port: source_port
   - ip_version: ip_version
   - destination_ip_address: destination_ip_address
   - firewall_policy_id: firewall_policy_id
   - shared: shared
   - action: action
   - position: position
   - destination_port: destination_port
   - id: id
   - name: name







