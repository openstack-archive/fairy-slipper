
Show IPSec policy
=================

.. rest_method::  GET /v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}

Shows details for an IPSec policy.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - ipsecpolicy_id: ipsecpolicy_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - ipsecpolicies: ipsecpolicies
   - description: description
   - tenant_id: tenant_id
   - ipsecpolicy: ipsecpolicy
   - auth_algorithm: auth_algorithm
   - encapsulation_mode: encapsulation_mode
   - encryption_algorithm: encryption_algorithm
   - pfs: pfs
   - value: value
   - transform_protocol: transform_protocol
   - units: units
   - lifetime: lifetime
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/vpn/ipsecpolicy-show-response.json
   :language: javascript






