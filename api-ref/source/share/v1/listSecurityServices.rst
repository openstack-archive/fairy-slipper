
List security services
======================

.. rest_method::  GET /v2/{tenant_id}/security-services

Lists all security services.


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
   - type: type
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-security-services-list-response.json
   :language: javascript



