
Update user
===========

.. rest_method::  PUT /v2.0/users/{userId}

Updates a user.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - userId: userId

Request Example
---------------

.. literalinclude:: ../samples/OS-KSADM/user-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - users: users
   - enabled: enabled
   - email: email
   - name: name
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/OS-KSADM/user-show-response.json
   :language: javascript












