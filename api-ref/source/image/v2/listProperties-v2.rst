
List property definitions
=========================

.. rest_method::  GET /v2/metadefs/namespaces/{namespace_id}/properties

Lists property definitions in a namespace.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - namespace_id: namespace_id



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
   - properties: properties
   - minLength: minLength
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/metadef-properties-list-response.json
   :language: javascript



