
Revoke role from user
=====================

.. rest_method::  DELETE /v3/OS-INHERIT/projects/{project_id}/users/{user_id}/roles/{role_id}/inherited_to_projects

Revokes an inherited role from a user in a project.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - role_id: role_id
   - project_id: project_id







