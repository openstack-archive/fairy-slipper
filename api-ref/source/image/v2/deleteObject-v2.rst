
Delete property definition
==========================

.. rest_method::  DELETE /v2/metadefs/namespaces/{namespace_id}/objects/{object_name}

Deletes an object definition from a namespace.

To delete a protected object from a namespace, you must first set
the ``protected`` attribute to false (boolean) on the namespace and
then perform the delete. If you try to delete a protected object,
the call returns the ``403`` response code.

When you successfully delete an object from a namespace, the
response is empty and the response code is ``204``.

Error response codes:403,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - object_name: object_name
   - namespace_id: namespace_id








