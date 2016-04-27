
Create user
===========

.. rest_method::  POST /v3/users

Creates a user.

Error response codes:201,413,415,405,404,403,401,400,503,409,


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

Request Example
---------------

.. literalinclude:: ../samples/admin/user-create-request.json
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














