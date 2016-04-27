
Associate policy and endpoint
=============================

.. rest_method::  PUT /v3/policies/{policy_id}/OS-ENDPOINT-POLICY/endpoints/{endpoint_id}

Associates a policy and an endpoint.

If an association already exists between the endpoint and another
policy, this call replaces that association.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - endpoint_id: endpoint_id
   - policy_id: policy_id







