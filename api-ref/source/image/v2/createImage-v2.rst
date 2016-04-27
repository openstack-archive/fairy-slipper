
Create image
============

.. rest_method::  POST /v2/images

(Since Image API v2.0) Creates a virtual machine (VM) image.

The ``Location`` response header contains the URI for the image.
The response body contains the new image entity.

Synchronous Postconditions

- With correct permissions, you can see the image status as
  ``queued`` through API calls.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - tags: tags
   - container_format: container_format
   - min_ram: min_ram
   - disk_format: disk_format
   - visibility: visibility
   - properties: properties
   - protected: protected
   - min_disk: min_disk
   - id: id

Request Example
---------------

.. literalinclude:: ../samples/image-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - min_ram: min_ram
   - status: status
   - virtual_size: virtual_size
   - name: name
   - tags: tags
   - updated_at: updated_at
   - checksum: checksum
   - created_at: created_at
   - disk_format: disk_format
   - locations: locations
   - visibility: visibility
   - properties: properties
   - self: self
   - owner: owner
   - protected: protected
   - file: file
   - container_format: container_format
   - min_disk: min_disk
   - size: size
   - id: id
   - schema: schema





