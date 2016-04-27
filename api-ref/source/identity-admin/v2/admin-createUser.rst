
Create user
===========

.. rest_method::  POST /v2.0/users

Creates a user.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenantId: tenantId
   - password: password
   - enabled: enabled
   - email: email
   - name: name
   - X-Auth-Token: X-Auth-Token

Request Example
---------------

.. literalinclude:: ../samples/admin/user-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - username: username
   - enabled: enabled
   - email: email
   - name: name
   - id: id














