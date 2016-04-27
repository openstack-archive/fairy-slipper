
Get namespaces details
======================

.. rest_method::  GET /v2/metadefs/namespaces/{namespace_id}

Gets details for a namespace.

The response body shows a single namespace entity with all details
including properties and objects.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - namespace_id: namespace_id






Response Example
----------------

.. literalinclude:: ../samples/metadef-namespace-details-response.json
   :language: javascript



