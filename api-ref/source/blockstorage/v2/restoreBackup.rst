
Restore backup
==============

.. rest_method::  POST /v2/{tenant_id}/backups/{backup_id}/restore

Restores a Block Storage backup to an existing or new Block Storage volume.

You must specify either the UUID or name of the volume. If you
specify both the UUID and name, the UUID takes priority.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - restore: restore
   - name: name
   - volume_id: volume_id
   - tenant_id: tenant_id
   - backup_id: backup_id

Request Example
---------------

.. literalinclude:: ../samples/backups/backup-restore-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - restore: restore
   - backup_id: backup_id
   - volume_id: volume_id





