
Preview stack
=============

.. rest_method::  POST /v1/{tenant_id}/stacks/preview

Previews a stack.


Normal response codes: 200
Error response codes:500,409,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - files: files
   - stack_name: stack_name
   - template_url: template_url
   - template: template
   - parameters: parameters
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: samples/stack-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - parent: parent
   - disable_rollback: disable_rollback
   - description: description
   - links: links
   - stack_name: stack_name
   - timeout_mins: timeout_mins
   - creation_time: creation_time
   - capabilities: capabilities
   - notification_topics: notification_topics
   - updated_time: updated_time
   - stack_owner: stack_owner
   - stack: stack
   - parameters: parameters
   - id: id
   - resources: resources
   - template_description: template_description




Response Example
----------------

.. literalinclude:: samples/stack-preview-response.json
   :language: javascript







