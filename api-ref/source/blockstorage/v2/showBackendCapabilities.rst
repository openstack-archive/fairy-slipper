
Show back-end capabilities
==========================

.. rest_method::  GET /v2/{tenant_id}/capabilities/{hostname}

Shows capabilities for a storage back end.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - hostname: hostname



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - pool_name: pool_name
   - description: description
   - volume_backend_name: volume_backend_name
   - namespace: namespace
   - visibility: visibility
   - driver_version: driver_version
   - vendor_name: vendor_name
   - properties: properties
   - storage_protocol: storage_protocol




Response Example
----------------

.. literalinclude:: ../samples/capabilities/backend-capabilities-response.json
   :language: javascript



