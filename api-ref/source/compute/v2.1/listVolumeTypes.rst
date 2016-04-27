
List volume types
=================

.. rest_method::  GET /v2.1/{tenant_id}/os-volume-types

Lists volume types.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - volume_types: volume_types
   - extra_specs: extra_specs
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/os-volumes/volume-types-list-response.json
   :language: javascript









