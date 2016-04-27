
Show configuration parameter details
====================================

.. rest_method::  GET /v1.0/{accountId}/datastores/versions/{datastore_version_id}/parameters/{parameter_name}

Displays details for a configuration parameter associated with a data store version.

Details include the type, minimum and maximum values, and whether
you must restart the instance after you change the parameter value.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - parameter_name: parameter_name
   - datastore_version_id: datastore_version_id
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-show-parameter-details.json
   :language: javascript













