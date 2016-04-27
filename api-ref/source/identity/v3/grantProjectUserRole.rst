
Grant role to user on project
=============================

.. rest_method::  PUT /v3/projects/{project_id}/users/{user_id}/roles/{role_id}

Grants a role to a user on a project.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - role_id: role_id
   - project_id: project_id
   - user_id: user_id
















