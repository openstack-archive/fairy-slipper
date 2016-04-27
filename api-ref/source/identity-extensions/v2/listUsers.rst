
List users
==========

.. rest_method::  GET /v2.0/users

Lists all users.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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

.. literalinclude:: ../samples/OS-KSADM/users-list-response.json
   :language: javascript











