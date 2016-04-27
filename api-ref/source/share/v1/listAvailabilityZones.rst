
List availability zones
=======================

.. rest_method::  GET /v2/{tenant_id}/availability-zones

Lists all availability zones.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - updated_at: updated_at
   - created_at: created_at
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-availability-zones-list-response.json
   :language: javascript



