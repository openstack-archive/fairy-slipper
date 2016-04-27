
Show configuration group details
================================

.. rest_method::  GET /v1.0/{accountId}/configurations/{configId}

Lists details about a configuration group, including its values.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - configId: configId
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-config-group-details-response.json
   :language: javascript













