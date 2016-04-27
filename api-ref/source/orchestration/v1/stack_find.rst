
Find stack
==========

.. rest_method::  GET /v1/{tenant_id}/stacks/{stack_name}

Finds the canonical URL for a stack.

Also works with verbs other than GET , so that you can perform PUT
and DELETE operations on a current stack. Set your client to follow
redirects. When redirecting, the request method should not change
as defined in RFC2626. However, in many clients the default
behavior is to change the method to GET when you receive a ``302``
response code because this behavior is ubiquitous in web browsers.

Error response codes:302,404,500,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - stack_name: stack_name
   - tenant_id: tenant_id











