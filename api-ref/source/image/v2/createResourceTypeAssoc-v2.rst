
Create resource type association
================================

.. rest_method::  POST /v2/metadefs/namespaces/{namespace_id}/resource_types

Creates a resource type association in a namespace.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - prefix: prefix
   - properties_target: properties_target
   - name: name
   - namespace_id: namespace_id

Request Example
---------------

.. literalinclude:: ../samples/metadef-resource-type-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - created_at: created_at
   - prefix: prefix
   - properties_target: properties_target
   - name: name
   - updated_at: updated_at





