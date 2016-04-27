
Detach replica
==============

.. rest_method::  PATCH /v1.0/{accountId}/instances/{instanceId}

Detaches a replica from its replication source.

If you created an instance that is a replica of a source instance,
you can detach the replica from the source. This can be useful if
the source becomes unavailable. In this case, you can detach the
replica from the source, making the replica a standalone database
instance. You can then take the new standalone instance and create
a new replica of that instance.

Error response codes:202,413,415,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - replica_of: replica_of
   - slave_of: slave_of
   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-detach-replica-request.json
   :language: javascript



















