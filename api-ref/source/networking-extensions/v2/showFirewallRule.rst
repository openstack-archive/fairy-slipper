
Show firewall rule details
==========================

.. rest_method::  GET /v2.0/fw/firewall_rules/{firewall_rule_id}

Shows details for a firewall rule.

If the user is not an administrative user and the firewall rule
object does not belong to the tenant account, this call returns the
``Forbidden (403)`` response code.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - firewall_rule_id: firewall_rule_id



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

.. literalinclude:: ../samples/firewalls/firewall-rule-show-response.json
   :language: javascript






