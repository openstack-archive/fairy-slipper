
Detach configuration group
==========================

.. rest_method::  PUT /v1.0/{accountId}/instances/{instanceId}

Detaches a configuration group from an instance.

When you pass in only an instance ID and omit the configuration ID,
this operation detaches any configuration group that was attached
to the instance.

Error response codes:202,413,415,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - configuration: configuration
   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-detach-config-grp-request.json
   :language: javascript



















