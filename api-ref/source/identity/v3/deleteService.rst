
Delete service
==============

.. rest_method::  DELETE /v3/services/{service_id}

Deletes a service.

If you try to delete a service that still has associated endpoints,
this call either deletes all associated endpoints or fails until
all endpoints are deleted.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_id: service_id
















