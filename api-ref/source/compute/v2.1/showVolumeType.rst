
Show volume type details
========================

.. rest_method::  GET /v2.1/{tenant_id}/os-volume-types/{volume_type_id}

Shows details for a volume type.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - volume_type_id: volume_type_id






Response Example
----------------

.. literalinclude:: ../samples/os-volumes/volume-type-show-response.json
   :language: javascript









