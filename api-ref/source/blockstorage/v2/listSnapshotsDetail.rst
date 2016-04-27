
List snapshots with details
===========================

.. rest_method::  GET /v2/{tenant_id}/snapshots/detail

Lists all Block Storage snapshots, with details, that the tenant can access.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - os-extended-snapshot-attributes:progress: os-extended-snapshot-attributes:progress
   - description: description
   - created_at: created_at
   - name: name
   - volume_id: volume_id
   - os-extended-snapshot-attributes:project_id: os-extended-snapshot-attributes:project_id
   - size: size
   - id: id
   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/volumes/snapshots-list-detailed-response.json
   :language: javascript



