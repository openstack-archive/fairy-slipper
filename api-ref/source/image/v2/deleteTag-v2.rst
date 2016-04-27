
Delete tag definition
=====================

.. rest_method::  DELETE /v2/metadefs/namespaces/tags/{namespace_id}/{tag_name}

Deletes a tag definition within a namespace.

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

   - tag_name: tag_name
   - namespace_id: namespace_id








