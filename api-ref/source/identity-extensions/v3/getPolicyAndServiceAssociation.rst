
Verify a policy and service-type endpoint association
=====================================================

.. rest_method::  GET /v3/policies/{policy_id}/OS-ENDPOINT-POLICY/services/{service_id}

Verifies an association between a policy and an endpoint of a service type.

A HEAD version of this API is also supported.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_id: service_id
   - policy_id: policy_id







