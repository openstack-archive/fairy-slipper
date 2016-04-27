
Create namespace
================

.. rest_method::  POST /v2/metadefs/namespaces

Creates a namespace.

The ``Location`` response header contains the newly-created URI for
the namespace.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/metadef-namespace-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - display_name: display_name
   - description: description
   - hypervisor_type: hypervisor_type
   - enum: enum
   - namespace: namespace
   - visibility: visibility
   - objects: objects
   - protected: protected
   - resource_type_associations: resource_type_associations
   - properties: properties





