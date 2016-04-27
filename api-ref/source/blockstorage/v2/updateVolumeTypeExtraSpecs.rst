
Update extra specs for a volume type
====================================

.. rest_method::  PUT /v2/{tenant_id}/types/{volume_type_id}

Updates the extra specifications that are assigned to a volume type.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - extra_specs: extra_specs
   - volume_type: volume_type
   - volume_type_id: volume_type_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-type-update-request.json
   :language: javascript




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



