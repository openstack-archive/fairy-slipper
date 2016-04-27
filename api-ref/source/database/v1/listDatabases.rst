
List instance databases
=======================

.. rest_method::  GET /v1.0/{accountId}/instances/{instanceId}/databases

Lists databases for an instance.

This operation returns only the user-defined databases and not the
system databases. Only the database administrator can view the
``mysql``, ``information_schema``, and ``lost+found`` system
databases.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-list-databases-response.json
   :language: javascript













