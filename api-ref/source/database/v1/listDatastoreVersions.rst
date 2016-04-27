
List datastore versions
=======================

.. rest_method::  GET /v1.0/{accountId}/datastores/{datastore_name}/versions

Lists the available versions of a data store.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - datastore_name: datastore_name
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-list-datastore-versions.json
   :language: javascript













