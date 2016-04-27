
Resize instance
===============

.. rest_method::  POST /v1.0/{accountId}/instances/{instanceId}/action

Resizes the memory for an instance.

If you provide a valid ``flavorRef``, this operation changes the
memory size of the instance, and restarts MySQL.

Error response codes:202,413,415,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-instance-resize-instance-request.json
   :language: javascript



















