
Update firewall rule
====================

.. rest_method::  PUT /v2.0/fw/firewall_rules/{firewall_rule_id}

Updates a firewall rule.


Normal response codes: 200
Error response codes:404,401,400,


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
   - firewall_rule_id: firewall_rule_id

Request Example
---------------

.. literalinclude:: ../samples/firewalls/firewall-rule-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/firewalls/firewall-rule-update-response.json
   :language: javascript






