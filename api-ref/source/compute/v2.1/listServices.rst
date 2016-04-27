
List Compute services
=====================

.. rest_method::  GET /v2.1/{tenant_id}/os-services

Lists all running Compute services for a tenant.

Includes reasons, if available, for why any services were disabled.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - binary: binary
   - zone: zone
   - state: state
   - updated_at: updated_at
   - host: host
   - services: services
   - forced_down: forced_down
   - disabled_reason: disabled_reason
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/os-services/v2.11/services-list-response.json
   :language: javascript



