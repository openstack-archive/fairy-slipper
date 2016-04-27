
Show property definition
========================

.. rest_method::  GET /v2/metadefs/namespaces/{namespace_id}/properties/{property_name}

Shows the definition for a property.

If you use the ``resource_type`` query parameter, the API removes
the prefix of the resource type from the property name before it
submits the query. This enables you to look for a property name
that starts with a prefix from an associated resource type.

The response body shows a single property entity.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - property_name: property_name
   - namespace_id: namespace_id
   - property_name: property_name
   - resource_type: resource_type



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




Response Example
----------------

.. literalinclude:: ../samples/metadef-property-details-response.json
   :language: javascript



