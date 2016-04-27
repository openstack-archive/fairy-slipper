
Restart instance
================

.. rest_method::  POST /v1.0/{accountId}/instances/{instanceId}/action

Restarts the database service for an instance.

The restart operation restarts only the MySQL instance. Restarting
MySQL erases any dynamic configuration settings that you make in
MySQL.

The MySQL service is unavailable until the instance restarts.

If the operation succeeds, it returns the ``Accepted (202)``
response code.

Error response codes:202,413,415,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-instance-restart-request.json
   :language: javascript



















