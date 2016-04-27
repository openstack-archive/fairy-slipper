
Attach volume to server
=======================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Attaches a volume to a server. Specify the ``os-attach`` action in the request body.

Preconditions

- Volume status must be ``available``.

- You should set ``instance_uuid`` or ``host_name``.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instance_uuid: instance_uuid
   - mountpoint: mountpoint
   - host_name: host_name
   - os-attach: os-attach
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-attach-request.json
   :language: javascript








