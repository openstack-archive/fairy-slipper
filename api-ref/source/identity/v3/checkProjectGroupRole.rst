
Check whether group has role on project
=======================================

.. rest_method::  HEAD /v3/projects/{project_id}/groups/{group_id}/roles/{role_id}

Validates that a group has a role on a project.

Error response codes:204,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - role_id: role_id
   - project_id: project_id
   - group_id: group_id














