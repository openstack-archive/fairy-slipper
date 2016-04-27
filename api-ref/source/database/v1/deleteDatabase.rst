
Delete database
===============

.. rest_method::  DELETE /v1.0/{accountId}/instances/{instanceId}/databases/{databaseName}

Deletes a database.

This operation also deletes all data that is associated with the
database.

Error response codes:202,413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - databaseName: databaseName
   - accountId: accountId

















