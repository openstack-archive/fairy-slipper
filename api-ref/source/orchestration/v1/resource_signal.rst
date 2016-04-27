
Send a signal to a resource
===========================

.. rest_method::  POST /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/resources/{resource_name}/signal

Sends a signal to a resource.

The contents of the request body depends on the resource to which
you send a signal.

Some resources cannot receive signals. If you send them a signal,
they return a 400 error code.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - resource_name: resource_name
   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id






Response Example
----------------

.. literalinclude:: 
   :language: javascript



