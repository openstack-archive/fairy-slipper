
Remove resource type association
================================

.. rest_method::  DELETE /v2/metadefs/namespaces/{namespace_id}/resource_types/{name}

Removes a resource type association in a namespace.

To remove an association, first make an update namespace request to
set the ``protected`` attribute to false (boolean) on the
namespace. Then, remove the association. If the operation succeeds,
the response returns the HTTP 204 status code.

If you try to remove resource type associations in a namespace with
the ``protected`` attribute set to true (boolean), the operation
fails and the response returns the HTTP 403 error code.

Error response codes:403,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - namespace_id: namespace_id
   - name: name








