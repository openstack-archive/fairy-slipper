
Show server group details
=========================

.. rest_method::  GET /v2.1/{tenant_id}/os-server-groups/{server_group_id}

Shows details for a server group.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - server_group_id: server_group_id
   - tenant_id: tenant_id



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

.. literalinclude:: ../samples/os-server-groups/server-group-show-response.json
   :language: javascript



