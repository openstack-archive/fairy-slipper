
Show volume metadata
====================

.. rest_method::  GET /v2/{tenant_id}/volumes/{volume_id}/metadata

Shows metadata for a volume.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - volume_id: volume_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/volumes/volume-metadata-show-response.json
   :language: javascript



