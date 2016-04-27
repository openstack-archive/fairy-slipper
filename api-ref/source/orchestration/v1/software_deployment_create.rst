
Create deployment
=================

.. rest_method::  POST /v1/{tenant_id}/software_deployments

Creates a software deployment.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - server_id: server_id
   - config_id: config_id
   - stack_user_project_id: stack_user_project_id
   - action: action
   - status_reason: status_reason
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: samples/deployment-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - server_id: server_id
   - config_id: config_id
   - output_values: output_values
   - creation_time: creation_time
   - updated_at: updated_at
   - input_values: input_values
   - action: action
   - status_reason: status_reason
   - id: id




Response Example
----------------

.. literalinclude:: samples/deployment-create-response.json
   :language: javascript



