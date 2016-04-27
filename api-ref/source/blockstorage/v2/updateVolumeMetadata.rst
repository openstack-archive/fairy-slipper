
Update volume metadata
======================

.. rest_method::  PUT /v2/{tenant_id}/volumes/{volume_id}/metadata

Updates metadata for a volume.

Replaces metadata items that match keys. Does not modify items that
are not in the request.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-metadata-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/volumes/volume-metadata-update-response.json
   :language: javascript



