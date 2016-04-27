
List volume types
=================

.. rest_method::  GET /v2/{tenant_id}/types

Lists volume types.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - sort_key: sort_key
   - sort_dir: sort_dir
   - limit: limit
   - marker: marker



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - volume_types: volume_types
   - extra_specs: extra_specs
   - name: name
   - volume_type: volume_type




Response Example
----------------

.. literalinclude:: ../samples/volumes/volume-types-list-response.json
   :language: javascript



