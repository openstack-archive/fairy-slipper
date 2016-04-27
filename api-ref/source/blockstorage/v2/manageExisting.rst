
Manage existing volume
======================

.. rest_method::  POST /v2/{tenant_id}/os-volume-manage

Creates a Block Storage volume by using existing storage rather than allocating new storage.

The caller must specify a reference to an existing storage volume
in the ref parameter in the request. Although each storage driver
might interpret this reference differently, the driver should
accept a reference structure that contains either a source-volume-
id or source-volume-name element, if possible.

The API chooses the size of the volume by rounding up the size of
the existing storage volume to the next gibibyte (GiB).

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

.. literalinclude:: ../samples/os-volume-manage/volume-manage-request.json
   :language: javascript








