
Log disabled Compute service information
========================================

.. rest_method::  PUT /v2.1/{tenant_id}/os-services/disable-log-reason

Logs information to the Compute service table about why a Compute service was disabled.

Specify the service by its host name and binary name.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - binary: binary
   - host: host
   - disabled_reason: disabled_reason
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-services/service-disable-log-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - binary: binary
   - host: host
   - disabled_reason: disabled_reason
   - service: service




Response Example
----------------

.. literalinclude:: ../samples/os-services/service-disable-log-response.json
   :language: javascript



