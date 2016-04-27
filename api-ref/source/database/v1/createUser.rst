
Create user
===========

.. rest_method::  POST /v1.0/{accountId}/instances/{instanceId}/users

Creates a user for a database instance.

Asynchronously provisions a new user for the database instance by
using the configuration that you define in the request object.
After the API validates the request and starts progress on the
provisioning process, the call returns the ``Accepted (202)``
response code.

If the API cannot fulfill the corresponding request due to
insufficient data or data that is not valid, the API returns the
``Bad Request (400)`` response code with information about the
nature of the failure. You cannot recover from validation errors.
You must correct the cause of the failure and the request again.

This table lists the required attributes for creating users:

**Required attributes for user**

+-----------------+---------------------------------------------------------------------+------------------------------------+----------+
|    Applies to   |                                 Name                                |            Description             | Required |
+-----------------+---------------------------------------------------------------------+------------------------------------+----------+
|       User      |                                 name                                | Name of the user for the database. |   Yes    |
+-----------------+---------------------------------------------------------------------+------------------------------------+----------+
|     password    |                  User password for database access.                 |                Yes                 |          |
+-----------------+---------------------------------------------------------------------+------------------------------------+----------+
| (database) name | Name of the database that the user can access. You must specify one |                 No                 |          |
|                 |                       or more database names.                       |                                    |          |
+-----------------+---------------------------------------------------------------------+------------------------------------+----------+

 **Notes**

- The operation grants the user all privileges on the databases.

- Do not use the ``root`` user name, which is reserved.

These tables list the valid characters for database names, user
names, and passwords.

**Valid characters in database name, user name, and password**

+---------------------------------------------------------------------------------------------------------------------------------+
|                                                            Character                                                            |
+---------------------------------------------------------------------------------------------------------------------------------+
|                                             Letters (upper and lower cases allowed)                                             |
+---------------------------------------------------------------------------------------------------------------------------------+
|                                                             Numbers                                                             |
+---------------------------------------------------------------------------------------------------------------------------------+
| ``@``, ``?``, ``#``, and spaces are allowed, but **not** at the beginning and end of the database name, user name, and password |
+---------------------------------------------------------------------------------------------------------------------------------+
|                             ``_`` is allowed anywhere in the database name, user name, and password                             |
+---------------------------------------------------------------------------------------------------------------------------------+

**Characters that are not allowed in database name, user name, and password**

+---------------------------------------------------------+
|                        Character                        |
+---------------------------------------------------------+
|                      Single quotes                      |
+---------------------------------------------------------+
|                      Double quotes                      |
+---------------------------------------------------------+
|                       Back quotes                       |
+---------------------------------------------------------+
|                        Semicolons                       |
+---------------------------------------------------------+
|                          Commas                         |
+---------------------------------------------------------+
|                       Back slashes                      |
+---------------------------------------------------------+
|                     Forward slashes                     |
+---------------------------------------------------------+
| Spaces at the front or end of the user name or password |
+---------------------------------------------------------+

**Length restrictions for database name, user name, and password**

+------------------------------+-----------------------------+
|         Restriction          |            Value            |
+------------------------------+-----------------------------+
| Database name maximum length |              64             |
+------------------------------+-----------------------------+
|   User name maximum length   |              16             |
+------------------------------+-----------------------------+
|   Password maximum length    | unlimited (no restrictions) |
+------------------------------+-----------------------------+

Error response codes:202,413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-create-users-request.json
   :language: javascript


















