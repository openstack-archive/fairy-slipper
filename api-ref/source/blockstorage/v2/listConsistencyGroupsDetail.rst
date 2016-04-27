
List consistency groups with details
====================================

.. rest_method::  GET /v2/{tenant_id}/consistencygroups/detail

Lists consistency groups with details.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - sort_key: sort_key
   - sort_dir: sort_dir
   - limit: limit
   - marker: marker



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - availability_zone: availability_zone
   - created_at: created_at
   - volume_types: volume_types
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/consistencygroups/consistency-groups-list-detailed-response.json
   :language: javascript



