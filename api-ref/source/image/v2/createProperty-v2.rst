
Create property
===============

.. rest_method::  POST /v2/metadefs/namespaces/{namespace_id}/properties

Creates a property definition in a namespace.

The schema is a subset of the JSON property definition schema.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - additionalItems: additionalItems
   - description: description
   - title: title
   - default: default
   - items: items
   - operators: operators
   - enum: enum
   - maximum: maximum
   - minItems: minItems
   - readonly: readonly
   - minimum: minimum
   - maxItems: maxItems
   - maxLength: maxLength
   - uniqueItems: uniqueItems
   - pattern: pattern
   - type: type
   - minLength: minLength
   - name: name
   - namespace_id: namespace_id

Request Example
---------------

.. literalinclude:: ../samples/metadef-property-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - additionalItems: additionalItems
   - description: description
   - title: title
   - default: default
   - items: items
   - operators: operators
   - enum: enum
   - maximum: maximum
   - minItems: minItems
   - readonly: readonly
   - minimum: minimum
   - maxItems: maxItems
   - maxLength: maxLength
   - uniqueItems: uniqueItems
   - pattern: pattern
   - type: type
   - minLength: minLength
   - name: name





