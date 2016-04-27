
List DNS domains
================

.. rest_method::  GET /v2.1/{tenant_id}/os-floating-ip-dns

Lists registered DNS domains published by the DNS drivers.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: ../samples/os-floating-ip-dns/floating-ip-dns-domains-list-response.json
   :language: javascript



