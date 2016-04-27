
Show image details
==================

.. rest_method::  GET /v2/images/{image_id}

(Since Image API v2.0) Shows details for an image.

The response body contains a single image entity.

Preconditions

- The image must exist.


Normal response codes: 200
Error response codes:404,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - image_id: image_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - container_format: container_format
   - min_ram: min_ram
   - updated_at: updated_at
   - file: file
   - owner: owner
   - id: id
   - size: size
   - self: self
   - disk_format: disk_format
   - direct_url: direct_url
   - schema: schema
   - status: status
   - tags: tags
   - visibility: visibility
   - locations: locations
   - min_disk: min_disk
   - properties: properties
   - name: name
   - checksum: checksum
   - created_at: created_at
   - protected: protected
   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/image-show-response.json
   :language: javascript




