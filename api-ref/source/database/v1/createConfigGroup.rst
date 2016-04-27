
Create configuration group
==========================

.. rest_method::  POST /v1.0/{accountId}/configurations

Creates a configuration group.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - datastore: datastore
   - values: values
   - name: name
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-create-config-grp-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: samples/db-create-config-grp-response.json
   :language: javascript













