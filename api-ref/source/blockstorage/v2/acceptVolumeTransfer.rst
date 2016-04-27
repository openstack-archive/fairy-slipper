
Accept volume transfer
======================

.. rest_method::  POST /v2/{tenant_id}/os-volume-transfer/{transfer_id}/accept

Accepts a volume transfer.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - auth_key: auth_key
   - transfer_id: transfer_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-volume-transfer/volume-transfer-accept-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - volume_id: volume_id
   - id: id
   - links: links
   - name: name





