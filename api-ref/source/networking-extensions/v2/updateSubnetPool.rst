
Update subnet pool
==================

.. rest_method::  PUT /v2.0/subnetpools/{subnetpool_id}

Updates a subnet pool.


Normal response codes: 200
Error response codes:404,403,401,400,


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
   - default_prefixlen: default_prefixlen
   - max_prefixlen: max_prefixlen
   - subnetpool_id: subnetpool_id

Request Example
---------------

.. literalinclude:: ../samples/subnets/subnetpool-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/subnets/subnetpool-update-response.json
   :language: javascript







