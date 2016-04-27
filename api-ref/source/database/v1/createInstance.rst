
Create database instance
========================

.. rest_method::  POST /v1.0/{accountId}/instances

Creates a database instance.

Asynchronously provisions a database instance. You must specify a
flavor and a volume size. The service provisions the instance with
a volume of the requested size, which serves as storage for the
database instance.

 **Notes**

- You can create only one database instance per POST request.

- You can create a database instance with one or more databases. You
  associate users with each database.

- The default binding for the MySQL instance is port 3306.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - users: users
   - password: password
   - datastore_version: datastore_version
   - name: name
   - flavorRef: flavorRef
   - characterSet: characterSet
   - replica_count: replica_count
   - instance: instance
   - collate: collate
   - databases: databases
   - datastore: datastore
   - configuration: configuration
   - type: type
   - replica_of: replica_of
   - size: size
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-create-instance-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - updated: updated
   - name: name
   - created: created
   - characterSet: characterSet
   - instance: instance
   - collate: collate
   - databases: databases
   - flavor: flavor
   - users: users




Response Example
----------------

.. literalinclude:: samples/db-create-instance-response.json
   :language: javascript













