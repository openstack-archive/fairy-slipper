
Update stack
============

.. rest_method::  PUT /v1/{tenant_id}/stacks/{stack_name}/{stack_id}

Updates a stack.

Error response codes:404,202,500,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - files: files
   - disable_rollback: disable_rollback
   - parameters: parameters
   - tags: tags
   - environment: environment
   - template_url: template_url
   - template: template
   - timeout_mins: timeout_mins
   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id

Request Example
---------------

.. literalinclude:: samples/stack-update-request.json
   :language: javascript












