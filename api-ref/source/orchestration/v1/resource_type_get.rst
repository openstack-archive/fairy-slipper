
Show resource schema
====================

.. rest_method::  GET /v1/{tenant_id}/resource_types/{type_name}

Shows the interface schema for a resource type.

A schema describes the properties that can be set on the resource,
their types, constraints, descriptions, and default values.
Additionally, the response shows the resource attributes and their
descriptions.


Normal response codes: 200
Error response codes:401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - type_name: type_name



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - required: required
   - update_allowed: update_allowed
   - support_status: support_status
   - attributes: attributes
   - type: type
   - properties: properties
   - resource_type: resource_type




Response Example
----------------

.. literalinclude:: samples/resource-schema-response.json
   :language: javascript





