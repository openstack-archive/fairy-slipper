
Reenable volume replication
===========================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Re-enables replication of a volume. Specify the ``volume-replica-reenable`` action in the request body.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-reenable-replica: os-reenable-replica
   - size: size
   - os-volume-replication:driver_data: os-volume-replication:driver_data
   - os-volume-replication:extended_status: os-volume-replication:extended_status
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-replica-reenable-request.json
   :language: javascript








