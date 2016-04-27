
Delete replication base instance
================================

.. rest_method::  POST /v1.0/{accountId}/instances/{instanceId}/action

Deletes the base instance in a replication set.

If the base instance becomes unreachable, you can use this
operation to delete the base instance.

This operation:

- Finds the replica that has processed the greatest number of
  transactions and picks that replica to use as the new base
  instance.

- Transfers the public IP of the old base instance to the new base
  instance (which is the newly-promoted replica).

- Deletes the old base instance.

- Takes all the instances in the replication set and makes them
  start replicating from the new base instance.

For ``instanceId``, pass in the instance ID of the unreachable base
instance.

Error response codes:202,413,415,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-instance-eject-replica-request.json
   :language: javascript



















