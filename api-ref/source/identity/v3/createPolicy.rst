
Create policy
=============

.. rest_method::  POST /v3/policies

Creates a policy.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - policy: policy
   - user_id: user_id
   - project_id: project_id
   - type: type
   - blob: blob

Request Example
---------------

.. literalinclude:: ../samples/admin/policy-create-request.json
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














