
Create firewall policy
======================

.. rest_method::  POST /v2.0/fw/firewall_policies

Creates a firewall policy.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - firewall_rules_id: firewall_rules_id
   - firewall_policy: firewall_policy
   - name: name
   - tenant_id: tenant_id
   - shared: shared
   - audited: audited
   - description: description

Request Example
---------------

.. literalinclude:: ../samples/firewalls/firewall-policy-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - firewall_policy: firewall_policy
   - name: name
   - firewall_rules: firewall_rules
   - tenant_id: tenant_id
   - audited: audited
   - shared: shared
   - id: id
   - description: description







