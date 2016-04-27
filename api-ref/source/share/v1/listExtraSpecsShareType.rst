
List extra specs
================

.. rest_method::  GET /v2/{tenant_id}/types/{share_type_id}/extra_specs

Lists the extra specifications for a share type.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - share_type_id: share_type_id
   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - snapshot_support: snapshot_support
   - extra_specs: extra_specs
   - driver_handles_share_servers: driver_handles_share_servers




Response Example
----------------

.. literalinclude:: ../samples/manila-share-types-extra-specs-list-response.json
   :language: javascript



