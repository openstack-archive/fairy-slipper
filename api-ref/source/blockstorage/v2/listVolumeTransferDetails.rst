
List volume transfers, with details
===================================

.. rest_method::  GET /v2/{tenant_id}/os-volume-transfer/detail

Lists volume transfers, with details.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - created_at: created_at
   - volume_id: volume_id
   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/os-volume-transfer/volume-transfers-list-detailed-response.json
   :language: javascript



