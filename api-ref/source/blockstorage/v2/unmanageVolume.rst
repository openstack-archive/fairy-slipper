
Unmanage volume
===============

.. rest_method::  POST /v2/{tenant_id}/volumes/{volume_id}/action

Removes a volume from Block Storage management without removing the back-end storage object that is associated with it. Specify the ``os-unmanage`` action in the request body.

Preconditions

- Volume status must be ``available``.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-unmanage: os-unmanage
   - tenant_id: tenant_id
   - volume_id: volume_id

Request Example
---------------

.. literalinclude:: ../samples/volumes/volume-unmanage-request.json
   :language: javascript








