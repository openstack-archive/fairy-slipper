
Abandon stack
=============

.. rest_method::  DELETE /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/abandon

Deletes a stack but leaves its resources intact, and returns data that describes the stack and its resources.

This method can be disabled from the server side. If it is
disabled, this call throws an exception.


Normal response codes: 200
Error response codes:404,500,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id






Response Example
----------------

.. literalinclude:: samples/stack-abandon-response.json
   :language: javascript







