
List configuration defaults
===========================

.. rest_method::  GET /v1.0/{accountId}/instances/{instanceId}/configuration

Lists the configuration defaults for an instance.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-list-cfg-defaults-response.json
   :language: javascript













