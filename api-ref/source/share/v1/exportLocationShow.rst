
Show single export location
===========================

.. rest_method::  GET /v2/{tenant_id}/share_instances/{share_instance_id}/export_locations/{export_location_id}




Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - export_location_id: export_location_id
   - tenant_id: tenant_id
   - share_instance_id: share_instance_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - created_at: created_at
   - updated_at: updated_at
   - preferred: preferred
   - is_admin_only: is_admin_only
   - share_instance_id: share_instance_id
   - path: path
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/manila-export-location-show-response.json
   :language: javascript



