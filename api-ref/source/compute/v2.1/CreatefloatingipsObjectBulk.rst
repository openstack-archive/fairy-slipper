
Create floating IPs
===================

.. rest_method::  POST /v2.1/{tenant_id}/os-floating-ips-bulk

Bulk-creates floating IPs.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - ip_range: ip_range
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-floating-ips-bulk/floating-ips-bulk-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-floating-ips-bulk/floating-ips-bulk-create-response.json
   :language: javascript



