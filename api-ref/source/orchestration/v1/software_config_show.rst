
Show configuration details
==========================

.. rest_method::  GET /v1/{tenant_id}/software_configs/{config_id}

Shows details for a software configuration.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - config_id: config_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - inputs: inputs
   - group: group
   - name: name
   - outputs: outputs
   - creation_time: creation_time
   - config: config
   - options: options




Response Example
----------------

.. literalinclude:: samples/config-show-response.json
   :language: javascript






