
List services
=============

.. rest_method::  GET /v2/{tenant_id}/services

Lists all services.


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
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/manila-services-list-response.json
   :language: javascript



