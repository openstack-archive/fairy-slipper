
Manage share snapshot
=====================

.. rest_method::  POST /v2/{tenant_id}/snapshots/manage

(Since API v2.12) Configures Shared File Systems to manage a share snapshot.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - share_id: share_id
   - display_name: display_name
   - description: description
   - provider_location: provider_location
   - driver_options: driver_options
   - display_description: display_description
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-snapshot-manage-request.json
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

.. literalinclude:: ../samples/manila-snapshot-manage-response.json
   :language: javascript



