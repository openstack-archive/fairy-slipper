
List users
==========

.. rest_method::  GET /v2.0/users

Lists all users.

To show detailed information about a user by name, include the
``name`` query parameter in the request.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - username: username
   - users: users
   - enabled: enabled
   - id: id
   - email: email
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/user-show-response.json
   :language: javascript











