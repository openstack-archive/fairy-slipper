
Promote replicated volume
=========================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Promotes a replicated volume. Specify the ``os-promote-replica`` action in the request body.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-promote-replica: os-promote-replica
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-replica-promote-request.json
   :language: javascript








