
Update volume type
==================

.. rest_method::  PUT /v2/{tenant_id}/types/{volume_type_id}

Updates a volume type.

To create an environment with multiple-storage back ends, you must
specify a volume type. The API spawns Block Storage volume back
ends as children to ``cinder-volume``, and keys them from a unique
queue. The API names the back ends ``cinder-volume.HOST.BACKEND``.
For example, ``cinder-volume.ubuntu.lvmdriver``. When you create a
volume, the scheduler chooses an appropriate back end for the
volume type to handle the request.

For information about how to use volume types to create multiple-
storage back ends, see `Configure multiple-storage back ends
<http://docs.openstack.org/admin-
guide/blockstorage_multi_backend.html>`_.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - volume_type: volume_type
   - volume_type_id: volume_type_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-type-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - is_public: is_public
   - extra_specs: extra_specs
   - description: description
   - volume_type: volume_type
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/volumes/volume-type-show-response.json
   :language: javascript



