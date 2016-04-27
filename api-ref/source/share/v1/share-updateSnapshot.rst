
Update share snapshot
=====================

.. rest_method::  PUT /v2/{tenant_id}/snapshots/{snapshot_id}

Updates a share snapshot.

You can update these attributes:

- ``display_name``, which also changes the ``name`` of the share
  snapshot.

- ``display_description``, which also changes the ``description`` of
  the share snapshot.

- ``is_public``. Changes the level of visibility.

If you try to update other attributes, they retain their previous
values.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - display_name: display_name
   - display_description: display_description
   - tenant_id: tenant_id
   - snapshot_id: snapshot_id

Request Example
---------------

.. literalinclude:: ../samples/manila-snapshot-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/manila-snapshot-update-response.json
   :language: javascript



