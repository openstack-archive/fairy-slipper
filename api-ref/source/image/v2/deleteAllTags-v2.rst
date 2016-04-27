
Delete all tag definitions
==========================

.. rest_method::  DELETE /v2/metadefs/namespaces/tags/{namespace_id}

Deletes all tag definitions within a namespace.

You cannot delete tags in a namespace with the 'protected'
attribute set to true (boolean); the response returns the HTTP 403
status code.

You must first set the ``protected`` attribute to false (boolean)
on the namespace and then perform the delete. The response is empty
and returns the HTTP 204 status code.

Error response codes:403,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - namespace: namespace
   - namespace_id: namespace_id








