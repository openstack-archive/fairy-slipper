
Create IKE policy
=================

.. rest_method::  POST /v2.0/vpn/ikepolicies

Creates an IKE policy.

The IKE policy is used for phases one and two negotiation of the
VPN connection. You can specify both the authentication and
encryption algorithms for connections.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - ikepolicy: ikepolicy
   - description: description
   - tenant_id: tenant_id
   - auth_algorithm: auth_algorithm
   - name: name
   - encryption_algorithm: encryption_algorithm
   - pfs: pfs
   - value: value
   - phase1_negotiation_mode: phase1_negotiation_mode
   - units: units
   - lifetime: lifetime
   - ike_version: ike_version

Request Example
---------------

.. literalinclude:: ../samples/vpn/ikepolicy-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - ikepolicy: ikepolicy
   - ikepolicies: ikepolicies
   - description: description
   - tenant_id: tenant_id
   - auth_algorithm: auth_algorithm
   - name: name
   - encryption_algorithm: encryption_algorithm
   - pfs: pfs
   - value: value
   - phase1_negotiation_mode: phase1_negotiation_mode
   - units: units
   - lifetime: lifetime
   - id: id
   - ike_version: ike_version







