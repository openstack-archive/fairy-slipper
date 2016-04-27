
Get stack template
==================

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/template

Gets a template for a stack.


Normal response codes: 200
Error response codes:404,500,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - outputs: outputs
   - heat_template_version: heat_template_version
   - description: description
   - parameters: parameters
   - resources: resources




Response Example
----------------

.. literalinclude:: samples/template-show-response.json
   :language: javascript







