
Register image
==============

.. rest_method::  POST /v1.1/{tenant_id}/images/{image_id}

Registers an image in the registry.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - username: username
   - description: description
   - image_id: image_id

Request Example
---------------

.. literalinclude:: ../samples/image-registry/image-register-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - username: username
   - updated: updated
   - description: description
   - created: created
   - image: image
   - tags: tags
   - minDisk: minDisk
   - name: name
   - progress: progress
   - minRam: minRam
   - id: id
   - metadata: metadata





