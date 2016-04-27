
List object definitions
=======================

.. rest_method::  GET /v2/metadefs/namespaces/{namespace_id}/objects

Lists object definitions in a namespace.

Returns a subset of the larger collection of namespaces and a link
that you can use to get the next set of namespaces. You should
always check for the presence of a ``next`` link and use it as the
URI in a subsequent HTTP GET request. You should follow this
pattern until a ``next`` link is no longer provided. The next link
preserves any query parameters that you send in your initial
request. You can use the ``first`` link to jump back to the first
page of the collection. If you prefer to paginate through
namespaces manually, use the ``limit`` and ``marker`` parameters.

Use the ``resource_types`` and ``visibility`` query parameters to
filter the response.

For example, set the ``resource_types`` query parameter to
``OS::Glance::Image,OS::Nova::Flavor`` to filter the response to
include only namespaces that are associated with the given resource
types.

You can sort the results of this operation by using the
``sort_key`` and ``sort_dir`` parameters. The API uses the natural
sorting of whatever namespace attribute is provided as the
``sort_key``.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - namespace_id: namespace_id
   - visibility: visibility
   - resource_types: resource_types
   - sort_key: sort_key
   - sort_dir: sort_dir



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - display_name: display_name
   - description: description
   - namespace: namespace
   - visibility: visibility
   - protected: protected
   - namespaces: namespaces
   - resource_type_associations: resource_type_associations




Response Example
----------------

.. literalinclude:: ../samples/metadef-objects-list-response.json
   :language: javascript



