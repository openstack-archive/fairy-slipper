
List consistency groups
=======================

.. rest_method::  GET /v2/{tenant_id}/consistencygroups

Lists consistency groups.


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

   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/consistencygroups/consistency-groups-list-response.json
   :language: javascript



