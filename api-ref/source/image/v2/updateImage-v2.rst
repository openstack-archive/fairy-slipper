
Update image
============

.. rest_method::  PATCH /v2/images/{image_id}

(Since Image API v2.0) Updates an image.

Depending on the referenced target location, this operation
performs one of these actions:

**Image update actions**

+--------------------------------------+----------------------------------------------------------+
| Target location                      | Update action                                            |
+--------------------------------------+----------------------------------------------------------+
| An array index                       | The API inserts a new value into the array at the index. |
+--------------------------------------+----------------------------------------------------------+
| An object member that does not exist | The API adds a member to the object.                     |
+--------------------------------------+----------------------------------------------------------+
| An object member that exists         | The member value is replaced.                            |
+--------------------------------------+----------------------------------------------------------+

The operation object must contain a ``value`` member that contains
the value to add. For example:

.. code-block:: json

   {
       "op": "add",
       "path": "/a/b/c",
       "value": [
           "foo",
           "bar"
       ]
   }

The target location must reference one of these values:

- The root of the target document. The value is the entire content
  of the target document.

- A member value to add to an object. The API adds the value to the
  object at the location. If the member already exists, the API
  replaces it with the value.

- An element to add to the array. The API adds the element value to
  the array at the location. The API shifts any element that is at
  or above the index one position to the right. The index must not
  be greater than the number of elements in the array. If you use
  the hyphen (-) character to index the end of the array, the API
  appends the value to the array. See `JavaScript Object Notation
  (JSON) Pointer <http://tools.ietf.org/html/rfc6901>`_.

Because this operation adds to existing objects and arrays, its
target location often does not exist.

The request body must conform to one of these media types:

- ``application/openstack-images-v2.0-json-patch``

- ``application/openstack-images-v2.1-json-patch`` (since Image API
  v2.2)

You can also use the PATCH method to add or remove image
properties.

For information about the PATCH method and the available media
types, see `Image API v2 HTTP PATCH media types
<http://specs.openstack.org/openstack/glance-specs/specs/api/v2
/http-patch-image-api-v2.html>`_.

Preconditions

- When you add a location to or replace a location in the image, you
  must set the ``disk_format`` and ``container_format`` parameters
  in the image.

- When you replace a location, that location must be previously set
  in the image.

Synchronous Postconditions

- With correct permissions, you can view the updated values of the
  attributes of the image.

- After you add a location to an image that had no location and with
  correct permissions, you can use API calls to view the image
  status as ``active``.

- After you remove all locations from the image and with correct
  permissions, you can use API calls to view the image status as
  ``queued``.

Troubleshooting

- If you cannot update locations, your request might be missing some
  information. Make sure that you meet the preconditions and run
  the request again. If the request fails again, review your API
  request.


Normal response codes: 200
Error response codes:404,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - url: url
   - path: path
   - op: op
   - value: value
   - metadata: metadata
   - image_id: image_id

Request Example
---------------

.. literalinclude:: ../samples/image-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/image-update-response.json
   :language: javascript




