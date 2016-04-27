
List IPSec policies
===================

.. rest_method::  GET /v2.0/vpn/ipsecpolicies

Lists all IPSec policies.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - ipsecpolicies: ipsecpolicies
   - description: description
   - tenant_id: tenant_id
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

.. literalinclude:: ../samples/vpn/ipsecpolicies-list-response.json
   :language: javascript





