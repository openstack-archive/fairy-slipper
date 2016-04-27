
List subnet pools
=================

.. rest_method::  GET /v2.0/subnetpools

Lists subnet pools to which the tenant has access.

Default policy settings returns exclusively subnet pools owned by
the tenant submitting the request, unless the request is submitted
by a user with administrative rights.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - default_quota: default_quota
   - tenant_id: tenant_id
   - created_at: created_at
   - updated_at: updated_at
   - prefixes: prefixes
   - min_prefixlen: min_prefixlen
   - address_scope_id: address_scope_id
   - ip_version: ip_version
   - shared: shared
   - default_prefixlen: default_prefixlen
   - subnetpools: subnetpools
   - id: id
   - max_prefixlen: max_prefixlen




Response Example
----------------

.. literalinclude:: ../samples/subnets/subnetpools-list-response.json
   :language: javascript




