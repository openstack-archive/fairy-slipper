
Delete Compute service
======================

.. rest_method::  DELETE /v2.1/{tenant_id}/os-services/{service_id}

Deletes a Compute service.

Specify the service by its host name and binary name.

Error response codes:404,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - binary: binary
   - host: host
   - tenant_id: tenant_id
   - service_id: service_id

Request Example
---------------

.. literalinclude:: ../samples/os-services/service-enable-request.json
   :language: javascript









