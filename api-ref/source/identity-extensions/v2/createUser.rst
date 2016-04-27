
Create user
===========

.. rest_method::  POST /v2.0/users

Creates a user.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - enabled: enabled
   - id: id
   - user: user
   - users_links: users_links
   - email: email

Request Example
---------------

.. literalinclude:: ../samples/OS-KSADM/userwithoutid-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - enabled: enabled
   - email: email
   - name: name
   - id: id














