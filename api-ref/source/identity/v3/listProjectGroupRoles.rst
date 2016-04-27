
List roles for group on project
===============================

.. rest_method::  GET /v3/projects/{project_id}/groups/{group_id}/roles

Lists roles for a group on a project.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project_id: project_id
   - group_id: group_id






Response Example
----------------

.. literalinclude:: ../samples/admin/project-group-roles-list-response.json
   :language: javascript










