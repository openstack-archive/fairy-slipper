
Find unique DNS entry
=====================

.. rest_method::  GET /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{name}

Finds a unique DNS entry for a domain and name.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - domain: domain
   - name: name






Response Example
----------------

.. literalinclude:: ../samples/os-floating-ip-dns/floating-ip-dns-entry-show-response.json
   :language: javascript



