
Show backup details
===================

.. rest_method::  GET /v2/{tenant_id}/backups/{backup_id}

Shows details for a backup.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - backup_id: backup_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - object_count: object_count
   - container: container
   - description: description
   - links: links
   - availability_zone: availability_zone
   - created_at: created_at
   - updated_at: updated_at
   - name: name
   - has_dependent_backups: has_dependent_backups
   - volume_id: volume_id
   - fail_reason: fail_reason
   - size: size
   - backup: backup
   - id: id
   - is_incremental: is_incremental




Response Example
----------------

.. literalinclude:: ../samples/backups/backup-show-response.json
   :language: javascript



