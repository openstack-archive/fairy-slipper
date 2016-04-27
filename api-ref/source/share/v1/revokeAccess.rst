
Revoke access
=============

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Revokes access from a share.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-deny_access: os-deny_access
   - access_id: access_id
   - share_id: share_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-actions-revoke-access-request.json
   :language: javascript








