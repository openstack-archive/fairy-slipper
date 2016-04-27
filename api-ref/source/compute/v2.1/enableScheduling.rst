
Enable scheduling for a Compute service
=======================================

.. rest_method::  PUT /v2.1/{tenant_id}/os-services/enable

Enables scheduling for a Compute service.

Specify the service by its host name and binary name.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - binary: binary
   - host: host
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-services/v2.11/service-enable-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - binary: binary
   - host: host
   - service: service




Response Example
----------------

.. literalinclude:: ../samples/os-services/v2.11/service-enable-response.json
   :language: javascript



