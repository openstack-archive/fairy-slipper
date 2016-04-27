
Attach configuration group
==========================

.. rest_method::  PUT /v1.0/{accountId}/instances/{instanceId}

Attaches a configuration group to an instance.

Error response codes:202,413,415,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - configuration: configuration
   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-attach-config-grp-request.json
   :language: javascript



















