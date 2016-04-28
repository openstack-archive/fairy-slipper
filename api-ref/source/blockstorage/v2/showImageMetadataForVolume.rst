
Show image metadata for volume
==============================

.. rest_method::  GET /v2/{tenant_id}/os-vol-image-meta

Shows image metadata for a volume.

When the request is made, the caller must specify a reference to an
existing storage volume in the ``ref`` element. Each storage driver
may interpret the existing storage volume reference differently but
should accept a reference structure containing either a ``source-
volume-id`` or ``source-volume-name`` element, if possible.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - availability_zone: availability_zone
   - bootable: bootable
   - volume_type: volume_type
   - name: name
   - volume: volume
   - host: host
   - ref: ref
   - metadata: metadata
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-vol-image-meta/image-metadata-show-request.json
   :language: javascript








