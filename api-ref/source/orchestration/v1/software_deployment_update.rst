
Update deployment
=================

.. rest_method::  PUT /v1/{tenant_id}/software_deployments/{deployment_id}

Updates a software deployment.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - action: action
   - output_values: output_values
   - config_id: config_id
   - status: status
   - status_reason: status_reason
   - tenant_id: tenant_id
   - deployment_id: deployment_id

Request Example
---------------

.. literalinclude:: samples/deployment-update-request.json
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

.. literalinclude:: samples/deployment-update-response.json
   :language: javascript



