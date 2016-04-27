
Create volume type
==================

.. rest_method::  POST /v2/{tenant_id}/types

Creates a volume type.

To create an environment with multiple-storage back ends, you must
specify a volume type. Block Storage volume back ends are spawned
as children to ``cinder-volume``, and they are keyed from a unique
queue. They are named ``cinder-volume.HOST.BACKEND``. For example,
``cinder-volume.ubuntu.lvmdriver``. When a volume is created, the
scheduler chooses an appropriate back end to handle the request
based on the volume type.

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
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-type-create-request.json
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



