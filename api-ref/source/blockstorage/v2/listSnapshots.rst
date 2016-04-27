
List snapshots
==============

.. rest_method::  GET /v2/{tenant_id}/snapshots

Lists all Block Storage snapshots, with summary information, that the tenant can access.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - sort_key: sort_key
   - sort_dir: sort_dir
   - limit: limit
   - marker: marker



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - created_at: created_at
   - name: name
   - volume_id: volume_id
   - metadata: metadata
   - id: id
   - size: size




Response Example
----------------

.. literalinclude:: ../samples/volumes/snapshots-list-response.json
   :language: javascript



