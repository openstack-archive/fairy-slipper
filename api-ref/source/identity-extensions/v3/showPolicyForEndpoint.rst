
Show policy for endpoint
========================

.. rest_method::  GET /v3/policies/{policy_id}/OS-ENDPOINT-POLICY/policy

Shows a policy for an endpoint.

The extension finds the policy by traversing the ordered sequence
of methods of association. The extension shows the policy for the
first association that it finds. If the region of the endpoint has
a parent, the extension examines the region associations up the
region tree in ascending order.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - policy_id: policy_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - policy: policy
   - type: type
   - blob: blob
   - links: links
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/OS-ENDPOINT-POLICY/policy-show-response.json
   :language: javascript



