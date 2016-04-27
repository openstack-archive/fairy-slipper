
Replace all tags
================

.. rest_method::  PUT /v2.0/{resource_type}/{resource_id}/tags

Replaces all tags on the resource.


Normal response codes: 200
Error response codes:404,401,400,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tags: tags
   - resource_type: resource_type
   - resource_id: resource_id

Request Example
---------------

.. literalinclude:: ../samples/tag/tag-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - tags: tags




Response Example
----------------

.. literalinclude:: ../samples/tag/tag-update-response.json
   :language: javascript








