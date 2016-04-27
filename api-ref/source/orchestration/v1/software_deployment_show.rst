
Show deployment details
=======================

.. rest_method::  GET /v1/{tenant_id}/software_deployments/{deployment_id}

Shows details for a software deployment.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - deployment_id: deployment_id



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

.. literalinclude:: samples/deployment-show-response.json
   :language: javascript



