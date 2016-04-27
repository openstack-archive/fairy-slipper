
Show share type access details
==============================

.. rest_method::  GET /v2/{tenant_id}/types/{share_type_id}/share_type_access

Shows access details for a share type.

You can view access details for private share types only.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - share_type_id: share_type_id
   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - share_type_id: share_type_id
   - project_id: project_id




Response Example
----------------

.. literalinclude:: ../samples/manila-share-types-list-access-response.json
   :language: javascript



