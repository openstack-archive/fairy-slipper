
Validate template
=================

.. rest_method::  POST /v1/{tenant_id}/validate

Validates a template.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - environment: environment
   - template_url: template_url
   - template: template
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: samples/template-validate-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - ParameterGroups: ParameterGroups
   - Description: Description
   - Parameters: Parameters




Response Example
----------------

.. literalinclude:: samples/template-validate-response.json
   :language: javascript



