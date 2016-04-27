
Delete user
===========

.. rest_method::  DELETE /v1.0/{accountId}/instances/{instanceId}/users/{name}

Deletes a user for a database instance.

Do not use periods in user names. A bug in a Python library that
Rackspace uses that can cause incorrect user deletions to occur if
you use a period (.) in the user name. In this case, the bug in the
library truncates the user name to the portion from the beginning
up to the period. For example, for the ``my.userA`` user, the bug
truncates the user name to ``my``, and if the ``user`` exists, that
user is incorrectly deleted.

Error response codes:202,413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId

















