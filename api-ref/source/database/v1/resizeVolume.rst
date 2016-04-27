
Resize instance volume
======================

.. rest_method::  POST /v1.0/{accountId}/instances/{instanceId}/action

Resizes the volume that is attached to an instance.

You can use this operation to increase but not decrease the volume
size. A valid volume size is an integer value in gigabytes (GB).

You cannot increase the volume to a size that is larger than the
API volume size limit.

If this operation succeeds, it returns a 202 Accepted response.

Error response codes:202,413,415,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-instance-resize-volume-request.json
   :language: javascript



















