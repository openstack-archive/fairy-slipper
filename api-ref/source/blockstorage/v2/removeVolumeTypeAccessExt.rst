
Remove private volume type access
=================================

.. rest_method::  POST /v2/{tenant_id}/types/{volume_type}/action

Removes private volume type access from a project.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project: project
   - tenant_id: tenant_id
   - volume_type: volume_type

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-type-access-delete-request.json
   :language: javascript








