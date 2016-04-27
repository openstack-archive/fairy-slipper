
List default share types
========================

.. rest_method::  GET /v2/{tenant_id}/types/default

Lists default share types.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - os-share-type-access:is_public: os-share-type-access:is_public
   - required_extra_specs: required_extra_specs
   - name: name
   - driver_handles_share_servers: driver_handles_share_servers
   - extra_specs: extra_specs
   - snapshot_support: snapshot_support
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/manila-share-types-default-list-response.json
   :language: javascript



