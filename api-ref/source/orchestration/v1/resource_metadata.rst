
Show resource metadata
======================

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/resources/{resource_name}/metadata

Shows metadata for a resource.


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

.. literalinclude:: samples/resource-metadata-response.json
   :language: javascript



