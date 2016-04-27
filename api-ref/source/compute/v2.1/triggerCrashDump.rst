
Trigger crash dump in server (trigger_crash_dump action)
========================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Trigger a crash dump in a server.

Specify the ``trigger_crash_dump`` action in the request body.

When a crash dump is triggered for a virtual server, it causes a
system reboot. This action can cause data loss. Also, network
connectivity can be lost. Once the server comes back online, you
can find a Kernel Crash Dump file in a certain location of the
filesystem. For example, for Ubuntu you can find it in the
``/var/crash`` directory.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - trigger_crash_dump: trigger_crash_dump
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/server-action-trigger-crash-dump.json
   :language: javascript








