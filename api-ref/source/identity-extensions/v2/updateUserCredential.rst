
Update user credentials
=======================

.. rest_method::  POST /v2.0/users/{userId}/OS-KSADM/credentials/OS-KSEC2:ec2Credentials

Updates credentials for a user.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/OS-KSEC2/ec2Credentials-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/OS-KSEC2/ec2Credentials-show-response.json
   :language: javascript












