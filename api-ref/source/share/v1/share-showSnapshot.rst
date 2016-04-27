
Show share snapshot details
===========================

.. rest_method::  GET /v2/{tenant_id}/snapshots/{snapshot_id}

Shows details for a share snapshot.


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
   - share_id: share_id
   - description: description
   - created_at: created_at
   - share_proto: share_proto
   - share_size: share_size
   - size: size
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-snapshot-show-response.json
   :language: javascript



