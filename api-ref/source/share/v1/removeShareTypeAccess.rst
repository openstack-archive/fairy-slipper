
Remove share type access
========================

.. rest_method::  POST /v2/{tenant_id}/types/{share_type_id}/action

Removes share type access from a project.

You can remove access from private share types only.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project: project
   - share_type_id: share_type_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-type-revoke-access-request.json
   :language: javascript








