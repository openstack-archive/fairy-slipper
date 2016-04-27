
Check whether user has role on project
======================================

.. rest_method::  HEAD /v3/projects/{project_id}/users/{user_id}/roles/{role_id}

Validates that a user has a role on a project.

Error response codes:204,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - role_id: role_id
   - project_id: project_id
   - user_id: user_id














