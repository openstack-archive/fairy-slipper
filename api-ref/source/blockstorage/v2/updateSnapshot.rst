
Update snapshot
===============

.. rest_method::  PUT /v2/{tenant_id}/snapshots/{snapshot_id}

Updates a snapshot.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - snapshot: snapshot
   - description: description
   - name: name
   - tenant_id: tenant_id
   - snapshot_id: snapshot_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/snapshot-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - created_at: created_at
   - name: name
   - snapshot: snapshot
   - volume_id: volume_id
   - metadata: metadata
   - id: id
   - size: size




Response Example
----------------

.. literalinclude:: ../samples/volumes/snapshot-update-response.json
   :language: javascript



