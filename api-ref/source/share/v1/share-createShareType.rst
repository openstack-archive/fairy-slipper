
Create share type
=================

.. rest_method::  POST /v2/{tenant_id}/types

Creates a share type.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-share-type-access:is_public: os-share-type-access:is_public
   - snapshot_support: snapshot_support
   - extra_specs: extra_specs
   - name: name
   - driver_handles_share_servers: driver_handles_share_servers
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-type-create-request.json
   :language: javascript




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

.. literalinclude:: ../samples/manila-share-type-create-response.json
   :language: javascript



