
Find stack resources
====================

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}/resources

Finds the canonical URL for a resource list of a stack.

The canonical URL is returned for only non-deleted stacks. To fetch
the resource list for deleted stacks, use the following endpoint:

::

   /v1/{tenant_id}/stacks/{stack_name}/{stack_id}/resources

Error response codes:302,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id







