
Adopt stack
===========

.. rest_method::  POST /v1/{tenant_id}/stacks

Creates a stack from existing resources.

Error response codes:201,500,409,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - files: files
   - disable_rollback: disable_rollback
   - parameters: parameters
   - stack_name: stack_name
   - adopt_stack_data: adopt_stack_data
   - environment: environment
   - timeout_mins: timeout_mins
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: samples/stack-adopt-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: id
   - links: links
   - stack: stack









