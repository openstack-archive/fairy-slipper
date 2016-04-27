
Create volume metadata
======================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/metadata

Creates metadata for a volume.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-metadata-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata





