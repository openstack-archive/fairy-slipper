
Update property definition
==========================

.. rest_method::  PUT /v2/metadefs/namespaces/{namespace_id}/properties/{property_name}

Updates a property definition.


Normal response codes: 200
Error response codes:


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
   - property_name: property_name
   - maxItems: maxItems
   - maxLength: maxLength
   - uniqueItems: uniqueItems
   - pattern: pattern
   - type: type
   - minLength: minLength
   - namespace_id: namespace_id
   - property_name: property_name

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




Response Example
----------------

.. literalinclude:: ../samples/metadef-property-update-response.json
   :language: javascript



