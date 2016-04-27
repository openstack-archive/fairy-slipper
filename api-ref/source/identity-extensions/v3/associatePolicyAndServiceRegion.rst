
Associate policy and service-type endpoint in a region
======================================================

.. rest_method::  PUT /v3/policies/{policy_id}/OS-ENDPOINT-POLICY/services/regions/{region_id}

Associates a policy and an endpoint of a service type in a region.

If an association already exists between the service in a region
and another policy, this call replaces that association.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - region_id: region_id
   - policy_id: policy_id







