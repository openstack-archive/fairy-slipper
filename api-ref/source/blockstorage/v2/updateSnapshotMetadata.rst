
Update snapshot metadata
========================

.. rest_method::  PUT /v2/{tenant_id}/snapshots/{snapshot_id}/metadata

Updates metadata for a snapshot.

Replaces metadata items that match keys. Does not modify items that
are not in the request.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata
   - tenant_id: tenant_id
   - snapshot_id: snapshot_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/snapshot-metadata-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/volumes/snapshot-metadata-update-response.json
   :language: javascript



