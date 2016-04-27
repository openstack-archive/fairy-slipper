
Create or update DNS entry
==========================

.. rest_method::  PUT /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{name}

Creates or updates a DNS entry.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - domain: domain
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/os-floating-ip-dns/floating-ip-dns-create-or-update-entry-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-floating-ip-dns/floating-ip-dns-create-or-update-entry-response.json
   :language: javascript



