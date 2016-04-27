
List roles for user on project
==============================

.. rest_method::  GET /v3/projects/{project_id}/users/{user_id}/roles

Lists roles for a user on a project.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project_id: project_id
   - user_id: user_id






Response Example
----------------

.. literalinclude:: ../samples/admin/project-user-roles-list-response.json
   :language: javascript










