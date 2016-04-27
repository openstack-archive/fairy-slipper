
Update firewall policy
======================

.. rest_method::  PUT /v2.0/fw/firewall_policies/{firewall_policy_id}

Updates a firewall policy.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - firewall_policy_id: firewall_policy_id

Request Example
---------------

.. literalinclude:: ../samples/firewalls/firewall-policy-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/firewalls/firewall-policy-update-response.json
   :language: javascript






