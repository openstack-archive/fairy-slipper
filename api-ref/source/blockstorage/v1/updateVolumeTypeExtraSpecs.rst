
Update extra specs for a volume type
====================================

.. rest_method::  PUT /v1/{tenant_id}/types/{volume_type_id}

Updates the extra specifications for a volume type.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - extra_specs: extra_specs
   - name: name
   - volume_type: volume_type
   - tenant_id: tenant_id
   - volume_type_id: volume_type_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-type-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - extra_specs: extra_specs
   - name: name
   - volume_type: volume_type




Response Example
----------------

.. literalinclude:: ../samples/volumes/volume-type-show-response.json
   :language: javascript



