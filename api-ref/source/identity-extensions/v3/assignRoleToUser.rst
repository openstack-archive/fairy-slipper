
Assign role to user
===================

.. rest_method::  PUT /v3/OS-INHERIT/projects/{project_id}/users/{user_id}/roles/{role_id}/inherited_to_projects

Assigns a role to a user in projects in a subtree.

The API anchors the inherited role assignment to a project and
applies it to its subtree in the projects hierarchy to both
existing and future projects.

A user can have both a regular, non-inherited role assignment and
an inherited role assignment in the same project.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - role_id: role_id
   - project_id: project_id







