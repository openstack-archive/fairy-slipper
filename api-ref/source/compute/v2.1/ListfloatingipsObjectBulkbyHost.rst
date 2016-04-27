
List floating IPs by host
=========================

.. rest_method::  GET /v2.1/{tenant_id}/os-floating-ips-bulk/{host_name}

Lists all floating IPs for a host.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - host_name: host_name






Response Example
----------------

.. literalinclude:: ../samples/os-floating-ips-bulk/floating-ips-bulk-list-by-host-response.json
   :language: javascript



