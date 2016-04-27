
Show resource data
==================

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/resources/{resource_name}

Shows data for a resource.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - resource_name: resource_name
   - stack_name: stack_name
   - tenant_id: tenant_id
   - stack_id: stack_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - resource_name: resource_name
   - resource: resource
   - description: description
   - logical_resource_id: logical_resource_id
   - creation_time: creation_time
   - resource_status: resource_status
   - updated_time: updated_time
   - required_by: required_by
   - resource_status_reason: resource_status_reason
   - physical_resource_id: physical_resource_id
   - resource_type: resource_type




Response Example
----------------

.. literalinclude:: samples/resource-show-response.json
   :language: javascript






