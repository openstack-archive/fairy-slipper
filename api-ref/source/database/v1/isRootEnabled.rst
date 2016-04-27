
Show root-enabled status for database instance
==============================================

.. rest_method::  GET /v1.0/{accountId}/instances/{instanceId}/root

Shows root-enabled status for a database instance.

Returns ``true`` if root user is enabled for a database instance.
Otherwise, returns ``false``.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-check-root-user-response.json
   :language: javascript













