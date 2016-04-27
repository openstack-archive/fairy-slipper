
Update user
===========

.. rest_method::  PATCH /v3/users/{user_id}

Updates the password for or enables or disables a user.

If the back-end driver does not support this functionality, this
call might return the HTTP ``Not Implemented (501)`` response code.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - user: user
   - enabled: enabled
   - email: email
   - default_project_id: default_project_id
   - password: password
   - domain_id: domain_id
   - description: description
   - user_id: user_id

Request Example
---------------

.. literalinclude:: ../samples/admin/user-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - links: links
   - user: user
   - enabled: enabled
   - email: email
   - default_project_id: default_project_id
   - id: id
   - domain_id: domain_id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/user-update-response.json
   :language: javascript












