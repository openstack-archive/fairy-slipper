
List database instances
=======================

.. rest_method::  GET /v1.0/{accountId}/instances

Lists information, including status, for all database instances.

Lists status and information for all database instances.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-instances-index-response.json
   :language: javascript













