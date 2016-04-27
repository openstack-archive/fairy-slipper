
List deployments
================

.. rest_method::  GET /v1/{tenant_id}/software_deployments

Lists all available software deployments.


Normal response codes: 200
Error response codes:404,500,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



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

.. literalinclude:: samples/deployments-list-response.json
   :language: javascript







