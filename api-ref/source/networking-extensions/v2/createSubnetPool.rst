
Create subnet pool
==================

.. rest_method::  POST /v2.0/subnetpools

Creates a subnet pool.

Error response codes:201,404,403,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - default_quota: default_quota
   - tenant_id: tenant_id
   - subnetpool: subnetpool
   - prefixes: prefixes
   - min_prefixlen: min_prefixlen
   - address_scope_id: address_scope_id
   - shared: shared
   - default_prefixlen: default_prefixlen
   - max_prefixlen: max_prefixlen

Request Example
---------------

.. literalinclude:: ../samples/subnets/subnetpool-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - default_quota: default_quota
   - tenant_id: tenant_id
   - created_at: created_at
   - subnetpool: subnetpool
   - updated_at: updated_at
   - prefixes: prefixes
   - min_prefixlen: min_prefixlen
   - address_scope_id: address_scope_id
   - ip_version: ip_version
   - shared: shared
   - default_prefixlen: default_prefixlen
   - id: id
   - max_prefixlen: max_prefixlen









