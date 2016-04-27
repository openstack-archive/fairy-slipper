
Create volume
=============

.. rest_method::  POST /v2.1/{tenant_id}/os-volumes

Creates a volume.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - display_name: display_name
   - availability_zone: availability_zone
   - display_description: display_description
   - volume: volume
   - volume_type: volume_type
   - snapshot_id: snapshot_id
   - metadata: metadata
   - size: size
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-volumes/volume-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-volumes/volume-show-response.json
   :language: javascript









