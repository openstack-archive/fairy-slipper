
List stack events
=================

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/events

Lists events for a stack.


Normal response codes: 200
Error response codes:404,500,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id
   - resource_action: resource_action
   - resource_status: resource_status
   - resource_name: resource_name
   - resource_type: resource_type
   - limit: limit
   - marker: marker
   - sort_keys: sort_keys
   - sort_dir: sort_dir






Response Example
----------------

.. literalinclude:: samples/events-list-response.json
   :language: javascript







