
Show object definition
======================

.. rest_method::  GET /v2/metadefs/namespaces/{namespace_id}/objects/{object_name}

Shows the definition for an object.

The response body shows a single object entity.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - object_name: object_name
   - namespace_id: namespace_id






Response Example
----------------

.. literalinclude:: ../samples/metadef-object-details-response.json
   :language: javascript



