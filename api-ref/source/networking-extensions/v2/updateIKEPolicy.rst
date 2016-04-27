
Update IKE policy
=================

.. rest_method::  PUT /v2.0/vpn/ikepolicies/{ikepolicy_id}

Updates policy settings in an IKE policy.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - ikepolicy: ikepolicy
   - description: description
   - auth_algorithm: auth_algorithm
   - name: name
   - encryption_algorithm: encryption_algorithm
   - pfs: pfs
   - value: value
   - phase1_negotiation_mode: phase1_negotiation_mode
   - units: units
   - lifetime: lifetime
   - ike_version: ike_version
   - ikepolicy_id: ikepolicy_id

Request Example
---------------

.. literalinclude:: ../samples/vpn/ikepolicy-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/vpn/ikepolicy-update-response.json
   :language: javascript






