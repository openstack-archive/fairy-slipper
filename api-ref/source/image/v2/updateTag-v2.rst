
Update tag definition
=====================

.. rest_method::  PUT /v2/metadefs/namespaces/tags/{namespace_id}/{tag_name}

Renames a tag definition.


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

.. literalinclude:: ../samples/metadef-tag-update-response.json
   :language: javascript



