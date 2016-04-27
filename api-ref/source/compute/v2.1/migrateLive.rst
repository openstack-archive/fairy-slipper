
Live-migrate server (os-migrateLive action)
===========================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Live-migrates a server to a new host without rebooting.

Use the ``host`` parameter to specify the destination host. If you
omit this parameter, the scheduler chooses a host. If a scheduled
host is not suitable, the scheduler tries up to
``migrate_max_retries`` rescheduling attempts.

If both source and destination hosts provide local disks, you can
set the ``block_migration`` parameter to ``true``. If either host
uses shared storage, the migration fails if you set this parameter
to ``true``.

Policy defaults enable only users with the administrative role to
perform this operation. Cloud providers can change these
permissions through the ``policy.json`` file.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - disk_over_commit: disk_over_commit
   - block_migration: block_migration
   - host: host
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action-admin/os-migrateLive-request.json
   :language: javascript








