
Show stack details
==================

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/{stack_id}

Shows details for a stack.


Normal response codes: 200
Error response codes:404,500,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - parent: parent
   - updated_time: updated_time
   - description: description
   - links: links
   - stack_status_reason: stack_status_reason
   - stack_name: stack_name
   - outputs: outputs
   - tags: tags
   - creation_time: creation_time
   - capabilities: capabilities
   - notification_topics: notification_topics
   - timeout_mins: timeout_mins
   - stack_owner: stack_owner
   - stack_status: stack_status
   - stack: stack
   - parameters: parameters
   - id: id
   - stack_user_project_id: stack_user_project_id
   - template_description: template_description




Response Example
----------------

.. literalinclude:: samples/stack-show-response.json
   :language: javascript







