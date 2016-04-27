
Grant access
============

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Grants access to a share.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - allow_access: allow_access
   - access_level: access_level
   - access_type: access_type
   - access_to: access_to
   - share_id: share_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-actions-grant-access-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - share_id: share_id
   - created_at: created_at
   - updated_at: updated_at
   - access_type: access_type
   - access_to: access_to
   - access: access
   - access_level: access_level
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/manila-share-actions-grant-access-response.json
   :language: javascript



