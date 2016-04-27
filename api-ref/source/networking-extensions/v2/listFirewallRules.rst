
List firewall rules
===================

.. rest_method::  GET /v2.0/fw/firewall_rules

Lists all firewall rules.

The list might be empty.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - protocol: protocol
   - description: description
   - source_ip_address: source_ip_address
   - tenant_id: tenant_id
   - enabled: enabled
   - id: id
   - ip_version: ip_version
   - destination_ip_address: destination_ip_address
   - firewall_policy_id: firewall_policy_id
   - shared: shared
   - action: action
   - position: position
   - destination_port: destination_port
   - source_port: source_port
   - firewalls: firewalls
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/firewalls/firewall-rules-list-response.json
   :language: javascript





