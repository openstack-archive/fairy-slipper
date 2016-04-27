
Update IPSec policy
===================

.. rest_method::  PUT /v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}

Updates policy settings in an IPSec policy.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - transform_protocol: transform_protocol
   - ipsecpolicy: ipsecpolicy
   - auth_algorithm: auth_algorithm
   - encapsulation_mode: encapsulation_mode
   - encryption_algorithm: encryption_algorithm
   - pfs: pfs
   - value: value
   - units: units
   - lifetime: lifetime
   - name: name
   - ipsecpolicy_id: ipsecpolicy_id

Request Example
---------------

.. literalinclude:: ../samples/vpn/ipsecpolicy-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/vpn/ipsecpolicy-update-response.json
   :language: javascript






