
Enable service
==============

.. rest_method::  PUT /v2/{tenant_id}/services/enable

Enables a service.


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

.. literalinclude:: ../samples/manila-service-enable-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - disabled: disabled
   - binary: binary
   - host: host




Response Example
----------------

.. literalinclude:: ../samples/manila-service-enable-response.json
   :language: javascript



