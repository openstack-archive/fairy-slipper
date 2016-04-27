
Change password for user
========================

.. rest_method::  POST /v3/users/{user_id}/password

Changes the password for a user.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - original_password: original_password
   - password: password
   - user: user
   - user_id: user_id

Request Example
---------------

.. literalinclude:: ../samples/admin/user-password-update-request.json
   :language: javascript

















