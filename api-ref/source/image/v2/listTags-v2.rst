
List tags
=========

.. rest_method::  GET /v2/metadefs/namespaces/tags/{namespace_id}

Lists the tag definitions within a namespace.

To manually paginate through the list of tags, use the ``limit``
and ``marker`` parameters.

To sort the results of this operation use the ``sort_key`` and
``sort_dir`` parameters. The API uses the natural sort order of the
tag attribute of the ``sort_key`` parameter.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - namespace: namespace
   - namespace_id: namespace_id
   - limit: limit
   - marker: marker
   - sort_key: sort_key
   - sort_dir: sort_dir



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - tags: tags




Response Example
----------------

.. literalinclude:: ../samples/metadef-tags-list-response.json
   :language: javascript



