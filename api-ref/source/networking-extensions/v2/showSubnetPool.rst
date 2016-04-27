
Show subnet pool
================

.. rest_method::  GET /v2.0/subnetpools/{subnetpool_id}

Shows information for a subnet pool.

Use the ``fields`` query parameter to filter the results.


Normal response codes: 200
Error response codes:404,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - subnetpool_id: subnetpool_id



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

.. literalinclude:: ../samples/subnets/subnetpool-show-response.json
   :language: javascript





