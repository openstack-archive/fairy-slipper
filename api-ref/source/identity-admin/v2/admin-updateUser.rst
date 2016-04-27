
Update user
===========

.. rest_method::  PUT /v2.0/users/{userId}

Updates a user.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - username: username
   - enabled: enabled
   - email: email
   - name: name
   - userId: userId

Request Example
---------------

.. literalinclude:: ../samples/admin/user-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - enabled: enabled
   - email: email
   - name: name
   - id: id














