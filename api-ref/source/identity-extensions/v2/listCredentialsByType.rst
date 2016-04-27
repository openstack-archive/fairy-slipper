
List credentials by type
========================

.. rest_method::  GET /v2.0/users/{userId}/OS-KSADM/credentials/OS-KSEC2:ec2Credentials/{type}

Lists credentials by type.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - type: type






Response Example
----------------

.. literalinclude:: ../samples/OS-KSADM/credentials-show-response.json
   :language: javascript











