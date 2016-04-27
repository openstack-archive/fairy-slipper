
Create object
=============

.. rest_method::  POST /v2/metadefs/namespaces/{namespace_id}/objects

Creates an object definition in a namespace.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - display_name: display_name
   - description: description
   - objects: objects
   - namespace: namespace
   - visibility: visibility
   - protected: protected
   - resource_type_associations: resource_type_associations
   - properties: properties
   - namespace_id: namespace_id

Request Example
---------------

.. literalinclude:: ../samples/metadef-object-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - display_name: display_name
   - description: description
   - objects: objects
   - namespace: namespace
   - visibility: visibility
   - protected: protected
   - resource_type_associations: resource_type_associations
   - properties: properties





