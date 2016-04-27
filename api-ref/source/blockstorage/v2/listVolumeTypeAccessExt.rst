
List private volume type access details
=======================================

.. rest_method::  GET /v2/{tenant_id}/types/{volume_type}/os-volume-type-access

Lists project IDs that have access to private volume type.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - volume_type: volume_type



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - project_id: project_id




Response Example
----------------

.. literalinclude:: ../samples/volumes/volume-type-access-list-response.json
   :language: javascript



