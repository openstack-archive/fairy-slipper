
Show snapshot metadata
======================

.. rest_method::  GET /v1/{tenant_id}/snapshots/{snapshot_id}/metadata

Shows metadata for a snapshot.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - snapshot_id: snapshot_id






Response Example
----------------

.. literalinclude:: ../samples/volumes/snapshot-metadata-show-response.json
   :language: javascript



