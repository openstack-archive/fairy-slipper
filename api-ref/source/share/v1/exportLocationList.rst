
List export locations
=====================

.. rest_method::  GET /v2/{tenant_id}/share_instances/{share_instance_id}/export_locations




Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - share_instance_id: share_instance_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - path: path
   - share_instance_id: share_instance_id
   - is_admin_only: is_admin_only
   - id: id
   - preferred: preferred




Response Example
----------------

.. literalinclude:: ../samples/manila-export-location-list-response.json
   :language: javascript



