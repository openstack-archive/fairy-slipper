
Check role for user
===================

.. rest_method::  HEAD /v3/OS-INHERIT/projects/{project_id}/users/{user_id}/roles/{role_id}/inherited_to_projects

Checks whether a user has a role assignment with the ``inherited_to_projects`` flag in a project.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - role_id: role_id
   - project_id: project_id






Response Example
----------------

.. literalinclude:: 
   :language: javascript



