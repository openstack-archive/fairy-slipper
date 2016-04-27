
List DNS entries
================

.. rest_method::  GET /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{ip}

Lists DNS entries for a domain and IP.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - domain: domain
   - ip: ip






Response Example
----------------

.. literalinclude:: ../samples/os-floating-ip-dns/floating-ip-dns-entry-by-ip-show-response.json
   :language: javascript



