
Add share type access
=====================

.. rest_method::  POST /v2/{tenant_id}/types/{share_type_id}/action

Adds share type access for a project.

You can add access to private share types only.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project: project
   - share_type_id: share_type_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-type-grant-access-request.json
   :language: javascript








