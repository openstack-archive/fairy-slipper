
Delete assisted volume snapshot
===============================

.. rest_method::  DELETE /v2.1/{tenant_id}/os-assisted-volume-snapshots/{snapshot_id}

Deletes an assisted volume snapshot.

To make this request, add the ``delete_info`` query parameter to
the URI, as follows:

.. code-block:: json

   DELETE /os-assisted-volume-snapshots?delete_info='{"volume_id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c"}'

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - snapshot_id: snapshot_id
   - delete_info: delete_info







