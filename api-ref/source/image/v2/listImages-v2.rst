
List images
===========

.. rest_method::  GET /v2/images

(Since Image API v2.0) Lists public virtual machine (VM) images.

Returns a subset of the larger collection of images and a link that
you can use to get the next set of images. You should always check
for the presence of a ``next`` link and use it as the URI in a
subsequent HTTP GET request. You should follow this pattern until a
``next`` link is no longer provided. The next link preserves any
query parameters that you send in your initial request. You can use
the ``first`` link to jump back to the first page of the
collection. If you prefer to paginate through images manually, use
the ``limit`` and ``marker`` parameters.

The list operation accepts query parameters to filter the response.

A client can provide direct comparison filters by using most image
attributes, such as ``name=Ubuntu``, ``visibility=public``, and so
on. A client cannot use tags or any ``link`` in the json-schema,
such as self, file, or schema, to filter the response.

You can use the ``size_min`` and ``size_max`` query parameters to
filter images that are greater than or less than the image size.
The size, in bytes, is the size of an image on disk.

For example, to filter the container to include only images that
are from 1 to 4 MB, set the ``size_min`` query parameter to
``1048576`` and the ``size_max`` query parameter to ``4194304``.

You can list VM images that have a status of ``active``,
``queued``, or ``saving``.

You can use query parameters to sort the results of this operation.

- ``sort_key``. Sorts by an image attribute. Sorts in the natural
  sorting direction of the image attribute.

- ``sort_dir``. Sorts in a sort direction.

- ``sort``. Sorts by one or more sets of attribute and sort
  direction combinations. If you omit the sort direction in a set,
  the default is ``desc``.

To sort the response, use the ``sort_key`` and ``sort_dir`` query
parameters:

.. code-block:: json

   GET /v2/images?sort_key=name
   &
   sort_dir=asc
   &
   sort_key=status
   &
   sort_dir=desc

Alternatively, specify the ``sort`` query parameter:

.. code-block:: json

   GET /v2/images?sort=name:asc,status:desc


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
   - name: name
   - visibility: visibility
   - member_status: member_status
   - owner: owner
   - status: status
   - size_min: size_min
   - size_max: size_max
   - sort_key: sort_key
   - sort_dir: sort_dir
   - sort: sort
   - tag: tag
   - created_at: created_at
   - updated_at: updated_at



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - min_ram: min_ram
   - status: status
   - virtual_size: virtual_size
   - name: name
   - tags: tags
   - checksum: checksum
   - created_at: created_at
   - size: size
   - disk_format: disk_format
   - updated_at: updated_at
   - owner: owner
   - self: self
   - min_disk: min_disk
   - protected: protected
   - visibility: visibility
   - file: file
   - container_format: container_format
   - images: images
   - schema: schema
   - id: id
   - first: first




Response Example
----------------

.. literalinclude:: ../samples/images-list-response.json
   :language: javascript



