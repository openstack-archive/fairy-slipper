
Create configuration
====================

.. rest_method::  POST /v1/{tenant_id}/software_configs

Creates a software configuration.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - inputs: inputs
   - group: group
   - name: name
   - outputs: outputs
   - config: config
   - options: options
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: samples/config-create-request.json
   :language: javascript




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

.. literalinclude:: samples/config-create-response.json
   :language: javascript






