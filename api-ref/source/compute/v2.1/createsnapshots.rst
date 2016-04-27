
Create assisted volume snapshots
================================

.. rest_method::  POST /v2.1/{tenant_id}/os-assisted-volume-snapshots

Creates an assisted volume snapshot.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - new_file: new_file
   - volume_id: volume_id
   - snapshot: snapshot
   - snapshot_id: snapshot_id
   - create_info: create_info
   - type: type
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-assisted-volume-snapshots/snapshot-create-assisted-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: id
   - volume_id: volume_id




Response Example
----------------

.. literalinclude:: ../samples/os-assisted-volume-snapshots/snapshot-create-assisted-response.json
   :language: javascript



