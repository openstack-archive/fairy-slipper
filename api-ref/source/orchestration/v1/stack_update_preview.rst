
Preview stack update
====================

.. rest_method::  PUT /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/preview

Previews an update for a stack.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - files: files
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







Response Example
----------------

.. literalinclude:: samples/stack-update-preview-response.json
   :language: javascript



