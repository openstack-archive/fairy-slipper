
Add tag definition
==================

.. rest_method::  POST /v2/metadefs/namespaces/tags/{namespace_id}/{tag_name}

Adds a tag to the list of namespace tag definitions.


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

.. literalinclude:: ../samples/metadef-tag-add-response.json
   :language: javascript



