
Promote instance to replica source
==================================

.. rest_method::  POST /v1.0/{accountId}/instances/{instanceId}/action

Promotes a replica.

If you have set up replication, and the base instance is still
reachable, you can use this operation to promote a replica to be
the new base instance.

This can be useful if you want to make a configuration change to
the base instance that your replicas are replicating from. For
example, you might want to increase the disk or CPU capacity. If
you made the change on the base instance directly, you would need
to take the base instance down for the duration of the operation.
Instead, you can create a replica, make the configuration change on
the replica, and then promote the replica to become the new base
instance.

For ``instanceId``, pass in the instance ID of the replica you want
to promote.

Error response codes:202,413,415,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-instance-promote-replica-request.json
   :language: javascript



















