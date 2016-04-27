
Remove property definition
==========================

.. rest_method::  DELETE /v2/metadefs/namespaces/{namespace_id}/properties/{property_name}

Removes a property definition in a namespace.

To remove a property, first make an update namespace request to set
the ``protected`` attribute to false (boolean) on the namespace.
Then, remove the property. If the operation succeeds, the response
returns the HTTP 204 status code.

If you try to remove a property in a namespace with the
``protected`` attribute set to true (boolean), the operation fails
and the response returns the HTTP 403 error code.

Error response codes:403,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - property_name: property_name
   - namespace_id: namespace_id
   - property_name: property_name








