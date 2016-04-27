
Update configuration group
==========================

.. rest_method::  PUT /v1.0/{accountId}/configurations/{configId}

Sets new values for a configuration group. Also lets you change the name and description of the configuration group.

Error response codes:202,413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - values: values
   - description: description
   - name: name
   - configId: configId
   - accountId: accountId

Request Example
---------------

.. literalinclude:: samples/db-update-config-grp-request.json
   :language: javascript


















