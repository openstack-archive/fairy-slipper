
Suspend stack
=============

.. rest_method::  POST /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions

Suspends a stack.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - suspend: suspend
   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id

Request Example
---------------

.. literalinclude:: samples/stack-action-suspend-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: 
   :language: javascript



