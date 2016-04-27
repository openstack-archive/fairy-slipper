
Show IKE policy details
=======================

.. rest_method::  GET /v2.0/vpn/ikepolicies/{ikepolicy_id}

Shows details for an IKE policy.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - ikepolicy_id: ikepolicy_id



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




Response Example
----------------

.. literalinclude:: ../samples/vpn/ikepolicy-show-response.json
   :language: javascript






