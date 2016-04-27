
List configuration groups
=========================

.. rest_method::  GET /v1.0/{accountId}/configurations

Lists all configuration groups.

The list includes the associated data store and data store version
for each configuration group.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-list-cfg-groups-response.json
   :language: javascript













