
List policy and service endpoint associations
=============================================

.. rest_method::  GET /v3/policies/{policy_id}/OS-ENDPOINT-POLICY/endpoints

Lists all the endpoints that are currently associated with a policy through any of the association methods.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - policy_id: policy_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - links: links
   - url: url
   - region: region
   - next: next
   - self: self
   - interface: interface
   - service_id: service_id
   - endpoints: endpoints
   - id: id
   - previous: previous




Response Example
----------------

.. literalinclude:: ../samples/OS-ENDPOINT-POLICY/policy-endpoint-associations-list-response.json
   :language: javascript



