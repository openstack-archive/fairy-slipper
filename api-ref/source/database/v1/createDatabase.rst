
Create database
===============

.. rest_method::  POST /v1.0/{accountId}/instances/{instanceId}/databases

Creates a database within an instance.

The ``name`` of the database is a required attribute.

Error response codes:202,413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - characterSet: characterSet
   - collate: collate
   - name: name
   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-create-databases-request.json
   :language: javascript


















