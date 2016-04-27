
Create server group
===================

.. rest_method::  POST /v2.1/{tenant_id}/os-server-groups

Creates a server group.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - server_groups: server_groups
   - name: name
   - policies: policies
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-server-groups/server-group-create-request.json
   :language: javascript




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

.. literalinclude:: ../samples/os-server-groups/server-group-create-response.json
   :language: javascript



