
List IKE policies
=================

.. rest_method::  GET /v2.0/vpn/ikepolicies

Lists IKE policies.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

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




Response Example
----------------

.. literalinclude:: ../samples/vpn/ikepolicies-list-response.json
   :language: javascript





