
List server groups
==================

.. rest_method::  GET /v2.1/{tenant_id}/os-server-groups

Lists all server groups for the tenant.

Administrative users can use the ``all_projects`` query parameter
to list all server groups for all projects.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - all_projects: all_projects



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - server_groups: server_groups
   - user_id: user_id
   - name: name
   - members: members
   - policies: policies
   - project_id: project_id
   - id: id
   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/os-server-groups/server-groups-list-response.json
   :language: javascript



