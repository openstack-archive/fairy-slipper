
List roles for user
===================

.. rest_method::  GET /v3/OS-INHERIT/projects/{project_id}/users/{user_id}/roles/inherited_to_projects

Lists the project roles that a user in a project inherits from a parent project.

The list shows only roles that the user project inherits from the
parent project.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - project_id: project_id






Response Example
----------------

.. literalinclude:: ../samples/OS-INHERIT/user-roles-list-response.json
   :language: javascript



