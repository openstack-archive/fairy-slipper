
Create IPSec policy
===================

.. rest_method::  POST /v2.0/vpn/ipsecpolicies

Creates an IP security (IPSec) policy.

The IPsec policy specifies the authentication and encryption
algorithms and encapsulation mode to use for the established VPN
connection.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

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
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/vpn/ipsecpolicy-create-request.json
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







