
List roles for group
====================

.. rest_method::  GET /v3/OS-INHERIT/projects/{project_id}/groups/{group_id}/roles/inherited_to_projects

Lists the project roles that a group in a project inherits from a parent project.

The list shows only roles that the group project inherits from the
parent project.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group_id: group_id
   - project_id: project_id






Response Example
----------------

.. literalinclude:: ../samples/OS-INHERIT/group-roles-list-response.json
   :language: javascript



