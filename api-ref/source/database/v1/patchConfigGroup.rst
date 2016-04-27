
Patch configuration group
=========================

.. rest_method::  PATCH /v1.0/{accountId}/configurations/{configId}

Sets new values for a configuration group.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - values: values
   - configId: configId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-patch-config-grp-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: samples/db-patch-config-grp-response-json-http.txt
   :language: javascript













