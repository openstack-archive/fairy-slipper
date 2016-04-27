
Extend volume size
==================

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Extends the size of a volume to a requested size, in gibibytes (GiB). Specify the ``os-extend`` action in the request body.

Preconditions

- Volume status must be ``available``.

- Sufficient amount of storage must exist to extend the volume.

- The user quota must have sufficient volume storage.

Troubleshooting

- An ``error_extending`` volume status indicates that the request
  failed. Ensure that you meet the preconditions and retry the
  request. If the request fails again, investigate the storage back
  end.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-extend: os-extend
   - new_size: new_size
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-extend-request.json
   :language: javascript








