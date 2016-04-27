
Update policy
=============

.. rest_method::  PATCH /v3/policies/{policy_id}

Updates a policy.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - policy: policy
   - user_id: user_id
   - project_id: project_id
   - type: type
   - blob: blob
   - policy_id: policy_id

Request Example
---------------

.. literalinclude:: ../samples/admin/policy-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/admin/policy-update-response.json
   :language: javascript












