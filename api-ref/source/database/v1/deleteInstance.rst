
Delete database instance
========================

.. rest_method::  DELETE /v1.0/{accountId}/instances/{instanceId}

Deletes a database instance, including any associated data.

This operation does not delete any read slaves.

You cannot complete this operation when the instance state is
either ``REBUILDING`` or ``BUILDING``.

Error response codes:202,413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId

















