
Update object definition
========================

.. rest_method::  PUT /v2/metadefs/namespaces/{namespace_id}/objects/{object_name}

Updates an object definition in a namespace.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - object_name: object_name
   - namespace_id: namespace_id

Request Example
---------------

.. literalinclude:: ../samples/metadef-object-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/metadef-object-update-response.json
   :language: javascript



