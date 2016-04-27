
Show volume type details
========================

.. rest_method::  GET /v2/{tenant_id}/types/{volume_type_id}

Shows details for a volume type.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - volume_type_id: volume_type_id
   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - is_public: is_public
   - extra_specs: extra_specs
   - description: description
   - volume_type: volume_type
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/volumes/volume-type-show-response.json
   :language: javascript



