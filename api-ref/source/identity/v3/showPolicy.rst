
Show policy details
===================

.. rest_method::  GET /v3/policies/{policy_id}

Shows details for a policy.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - policy_id: policy_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - links: links
   - blob: blob
   - policy: policy
   - project_id: project_id
   - type: type
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/admin/policy-show-response.json
   :language: javascript










