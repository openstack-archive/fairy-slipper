
Create or update DNS domain
===========================

.. rest_method::  PUT /v2.1/{tenant_id}/os-floating-ip-dns/{domain}

Creates or updates a DNS domain.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - domain: domain

Request Example
---------------

.. literalinclude:: ../samples/os-floating-ip-dns/floating-ip-dns-create-or-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-floating-ip-dns/floating-ip-dns-create-or-update-response.json
   :language: javascript



