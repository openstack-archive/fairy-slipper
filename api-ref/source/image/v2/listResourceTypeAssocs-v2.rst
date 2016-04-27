
List resource type associations
===============================

.. rest_method::  GET /v2/metadefs/namespaces/{namespace_id}/resource_types

Lists resource type associations in a namespace.

The response body lists resource type association entities.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - namespace_id: namespace_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - created_at: created_at
   - name: name
   - updated_at: updated_at




Response Example
----------------

.. literalinclude:: ../samples/metadef-resource-types-list-response.json
   :language: javascript



