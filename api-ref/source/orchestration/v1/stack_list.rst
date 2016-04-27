
List stack data
===============

.. rest_method::  GET /v1/{tenant_id}/stacks

Lists active stacks.


Normal response codes: 200
Error response codes:500,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - id: id
   - status: status
   - name: name
   - action: action
   - tenant: tenant
   - username: username
   - owner_id: owner_id
   - limit: limit
   - marker: marker
   - show_deleted: show_deleted
   - show_nested: show_nested
   - sort_keys: sort_keys
   - tags: tags
   - tags_any: tags_any
   - not_tags: not_tags
   - not_tags_any: not_tags_any
   - sort_dir: sort_dir
   - global_tenant: global_tenant
   - with_count: with_count



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - links: links
   - stack_status_reason: stack_status_reason
   - stack_name: stack_name
   - tags: tags
   - creation_time: creation_time
   - updated_time: updated_time
   - stack_status: stack_status
   - id: id




Response Example
----------------

.. literalinclude:: samples/stacks-list-response.json
   :language: javascript






