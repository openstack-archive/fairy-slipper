
List resource types
===================

.. rest_method::  GET /v1/{tenant_id}/resource_types

Lists all supported template resource types.


Normal response codes: 200
Error response codes:401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - name: name
   - version: version
   - support_status: support_status






Response Example
----------------

.. literalinclude:: samples/resource-types-list-response.json
   :language: javascript





