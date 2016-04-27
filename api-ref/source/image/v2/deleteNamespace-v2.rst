
Delete namespace
================

.. rest_method::  DELETE /v2/metadefs/namespaces/{namespace_id}

Deletes a namespace and its properties, objects, and any resource type associations.

You cannot delete namespaces with the ``protected`` attribute set
to ``true`` (boolean); the response returns the HTTP ``403``
response code.

To delete a namespace, you must first make an update namespace
request to set the ``protected`` attribute to false (boolean) on
the namespace. Then, delete the namespace.

A successful operation returns the HTTP ``204`` response code.

If you try to remove a namespace with the ``protected`` attribute
set to true (boolean), the operation fails and the response returns
the HTTP ``403`` response code.

Error response codes:403,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - namespace_id: namespace_id








