
Get tag definition
==================

.. rest_method::  GET /v2/metadefs/namespaces/tags/{namespace_id}/{tag_name}

Gets a definition for a tag.

The response body shows a single tag entity.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tag_name: tag_name
   - namespace_id: namespace_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name




Response Example
----------------

.. literalinclude:: ../samples/metadef-tag-details-response.json
   :language: javascript



