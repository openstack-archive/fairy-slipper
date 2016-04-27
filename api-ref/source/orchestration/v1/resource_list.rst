
List resources
==============

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/resources

Lists resources in a stack.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id
   - nested_depth: nested_depth
   - with_detail: with_detail



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - resource_name: resource_name
   - description: description
   - logical_resource_id: logical_resource_id
   - creation_time: creation_time
   - resource_status: resource_status
   - updated_time: updated_time
   - required_by: required_by
   - resources: resources
   - resource_status_reason: resource_status_reason
   - physical_resource_id: physical_resource_id
   - resource_type: resource_type




Response Example
----------------

.. literalinclude:: samples/resources-list-response.json
   :language: javascript






