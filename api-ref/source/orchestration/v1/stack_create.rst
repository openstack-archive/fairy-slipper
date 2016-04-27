
Create stack
============

.. rest_method::  POST /v1/{tenant_id}/stacks

Creates a stack.

Error response codes:201,500,409,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - files: files
   - disable_rollback: disable_rollback
   - parameters: parameters
   - tags: tags
   - stack_name: stack_name
   - environment: environment
   - template_url: template_url
   - template: template
   - timeout_mins: timeout_mins
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: samples/stack-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: id
   - links: links
   - stack: stack









