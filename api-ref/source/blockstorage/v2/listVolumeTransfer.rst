
List volume transfers
=====================

.. rest_method::  GET /v2/{tenant_id}/os-volume-transfer

Lists volume transfers.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - volume_id: volume_id
   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/os-volume-transfer/volume-transfers-list-response.json
   :language: javascript



