
Show resource template
======================

.. rest_method::  GET /v1/{tenant_id}/resource_types/{type_name}/template

Shows the template representation for a resource type.

The returned template contains a single resource type. Each
resource property is mapped to a template parameter and each
resource attribute is mapped to a template output.

You can use these templates as a starting place for creating
customized, template-based resources or as examples of using the
particular resource in another template.

Use the ``template_type`` query parameter to specify the resource
template type. Default type is ``cfn``. The ``hot`` template type
is supported. For example:

::

   /v1/{tenant_id}/resource_types/{type_name}/template?template_type=cfn


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - type_name: type_name



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Outputs: Outputs
   - HeatTemplateFormatVersion: HeatTemplateFormatVersion
   - Resources: Resources
   - Parameters: Parameters




Response Example
----------------

.. literalinclude:: samples/resource-type-template-response.json
   :language: javascript






