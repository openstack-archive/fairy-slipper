
List namespaces
===============

.. rest_method::  GET /v2/metadefs/namespaces

Lists public namespaces.

Returns a subset in the larger collection of namespaces and a link
that you can use to get the next set of namespaces. Check for the
presence of a ``next`` link and use it as the URI in a subsequent
HTTP GET request. Follow this pattern until a ``next`` link is no
longer provided. The ``next`` link preserves any query parameters
that you send in your initial request. You can use the ``first``
link to return to the first page in the collection. If you prefer
to paginate through namespaces manually, use the ``limit`` and
``marker`` parameters.

The list operation accepts the ``resource_types`` and
``visibility`` query parameters, which you can use to filter the
response.

To sort the results of this operation, use the ``sort_key`` and
``sort_dir`` parameters. The API uses the natural sorting order in
the namespace attribute that you provide as the ``sort_key``
parameter.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
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

.. literalinclude:: ../samples/metadef-namespaces-list-response.json
   :language: javascript



