
List database instance users
============================

.. rest_method::  GET /v1.0/{accountId}/instances/{instanceId}/users

Lists the users in a database instance and the associated databases for that user.

This operation does not return system users. A system user is a
database administrator who administers the health of the database.
Also, this operation returns the ``root`` user only if it is
enabled.

The following notes apply to MySQL users:

- User names can be up to 16 characters long.

- When you create accounts with INSERT, you must use FLUSH
  PRIVILEGES to tell the server to reload the grant tables.

- For additional information, See:
  `http://dev.mysql.com/doc/refman/5.1/en/user-account-
  management.html <http://dev.mysql.com/doc/refman/5.1/en/user-
  account-management.html>`_


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-list-users-response.json
   :language: javascript













