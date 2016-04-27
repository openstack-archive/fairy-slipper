
Associate policy and service-type endpoint
==========================================

.. rest_method::  PUT /v3/policies/{policy_id}/OS-ENDPOINT-POLICY/services/{service_id}

Associates a policy and any endpoint of a service type.

If an association already exists between the endpoint of a service
type and another policy, this call replaces that association.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_id: service_id
   - policy_id: policy_id







