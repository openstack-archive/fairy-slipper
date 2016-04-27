
List share snapshots with details
=================================

.. rest_method::  GET /v2/{tenant_id}/snapshots/detail

Lists all share snapshots with details.


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
   - share_id: share_id
   - description: description
   - created_at: created_at
   - share_proto: share_proto
   - share_size: share_size
   - size: size
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-snapshots-list-detailed-response.json
   :language: javascript



