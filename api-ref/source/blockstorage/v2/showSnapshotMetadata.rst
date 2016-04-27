
Show snapshot metadata
======================

.. rest_method::  GET /v2/{tenant_id}/snapshots/{snapshot_id}/metadata

Shows metadata for a snapshot.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - snapshot_id: snapshot_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - os-extended-snapshot-attributes:progress: os-extended-snapshot-attributes:progress
   - description: description
   - created_at: created_at
   - name: name
   - snapshot: snapshot
   - volume_id: volume_id
   - os-extended-snapshot-attributes:project_id: os-extended-snapshot-attributes:project_id
   - size: size
   - id: id
   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/volumes/snapshot-metadata-show-response.json
   :language: javascript



