
Show image details
==================

.. rest_method::  GET /v1.1/{tenant_id}/images/{image_id}

Shows details for an image.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - image_id: image_id



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




Response Example
----------------

.. literalinclude:: ../samples/image-registry/image-show-response.json
   :language: javascript



