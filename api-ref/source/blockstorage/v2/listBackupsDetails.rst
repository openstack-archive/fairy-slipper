
List backups with details
=========================

.. rest_method::  GET /v2/{tenant_id}/backups/detail

Lists Block Storage backups, with details, to which the tenant has access.


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
   - object_count: object_count
   - fail_reason: fail_reason
   - description: description
   - links: links
   - availability_zone: availability_zone
   - created_at: created_at
   - updated_at: updated_at
   - name: name
   - has_dependent_backups: has_dependent_backups
   - volume_id: volume_id
   - container: container
   - backups: backups
   - size: size
   - id: id
   - is_incremental: is_incremental




Response Example
----------------

.. literalinclude:: ../samples/backups/backups-list-detailed-response.json
   :language: javascript



