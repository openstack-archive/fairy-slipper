
List resource types
===================

.. rest_method::  GET /v2/metadefs/resource_types

Lists all resource types.

You can assign metadata definition namespaces to these resource
types. See the metadata definition resource types section.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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



