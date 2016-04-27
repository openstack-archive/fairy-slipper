
Delete volume
=============

.. rest_method::  DELETE /v2/{tenant_id}/volumes/{volume_id}

Deletes a volume.

Preconditions

- Volume status must be ``available``, ``in-use``, ``error``, or
  ``error_restoring``.

- You cannot already have a snapshot of the volume.

- You cannot delete a volume that is in a migration.

Asynchronous Postconditions

- The volume is deleted in volume index.

- The volume managed by OpenStack Block Storage is deleted in
  storage node.

Troubleshooting

- If volume status remains in ``deleting`` or becomes
  ``error_deleting`` the request failed. Ensure you meet the
  preconditions then investigate the storage back end.

- The volume managed by OpenStack Block Storage is not deleted from
  the storage system.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - volume_id: volume_id







