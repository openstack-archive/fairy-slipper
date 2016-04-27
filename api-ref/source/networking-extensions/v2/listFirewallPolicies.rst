
List firewall policies
======================

.. rest_method::  GET /v2.0/fw/firewall_policies

Lists all firewall policies.

The list might be empty.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - firewall_rules: firewall_rules
   - tenant_id: tenant_id
   - audited: audited
   - firewall_policies: firewall_policies
   - shared: shared
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/firewalls/firewall-policies-list-response.json
   :language: javascript





