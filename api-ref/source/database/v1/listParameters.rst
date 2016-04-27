
List configuration parameters
=============================

.. rest_method::  GET /v1.0/{accountId}/datastores/versions/{datastore_version_id}/parameters

Lists the available configuration parameters for a data store version.

Parameter information includes the type, minimum and maximum
values, and whether you must restart the instance after you change
a parameter value.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - datastore_version_id: datastore_version_id
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-list-parameters-response.json
   :language: javascript













