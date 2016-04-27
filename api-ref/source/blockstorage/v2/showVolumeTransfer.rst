
Show volume transfer details
============================

.. rest_method::  GET /v2/{tenant_id}/os-volume-transfer/{transfer_id}

Shows details for a volume transfer.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - transfer_id: transfer_id
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

.. literalinclude:: ../samples/os-volume-transfer/volume-transfer-show-response.json
   :language: javascript



