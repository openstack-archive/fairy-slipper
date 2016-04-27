
Check role for group
====================

.. rest_method::  HEAD /v3/OS-INHERIT/projects/{project_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects

Checks whether a group has a role assignment with the ``inherited_to_projects`` flag in a project.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group_id: group_id
   - role_id: role_id
   - project_id: project_id






Response Example
----------------

.. literalinclude:: 
   :language: javascript



