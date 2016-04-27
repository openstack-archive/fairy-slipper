
Create share snapshot
=====================

.. rest_method::  POST /v2/{tenant_id}/snapshots

Creates a snapshot from a share.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - share_id: share_id
   - force: force
   - description: description
   - display_description: display_description
   - display_name: display_name
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-snapshot-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - share_id: share_id
   - description: description
   - created_at: created_at
   - share_proto: share_proto
   - provider_location: provider_location
   - share_size: share_size
   - size: size
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-snapshot-create-response.json
   :language: javascript



