
Cancel stack update
===================

.. rest_method::  POST /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions

Cancels a currently running update of a stack.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - cancel_update: cancel_update
   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id

Request Example
---------------

.. literalinclude:: samples/stack-action-cancel-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: 
   :language: javascript



