
Create volume transfer
======================

.. rest_method::  POST /v2/{tenant_id}/os-volume-transfer

Creates a volume transfer.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - volume_id: volume_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-volume-transfer/volume-transfer-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - auth_key: auth_key
   - links: links
   - created_at: created_at
   - volume_id: volume_id
   - id: id
   - name: name





