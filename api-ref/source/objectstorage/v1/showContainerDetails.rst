
Show container details and list objects
=======================================

.. rest_method::  GET /v1/{account}/{container}

Shows details for a container and lists objects, sorted by name, in the container.

Specify query parameters in the request to filter the list and
return a subset of object names. Omit query parameters to return
the complete list of object names that are stored in the container,
up to 10,000 names. The 10,000 maximum value is configurable. To
view the value for the cluster, issue a GET ``/info`` request.

Example requests and responses:

- ``OK (200)``. Success. The response body lists the objects.

- ``No Content (204)``. Success. The response body shows no objects.
  Either the container has no objects or you are paging through a
  long list of names by using the ``marker``, ``limit``, or
  ``end_marker`` query parameter and you have reached the end of
  the list.

If the container does not exist, the call returns the ``Not Found
(404)`` response code.

The operation returns the ``Range Not Satisfiable (416)`` response
code for any ranged GET requests that specify more than:

- Fifty ranges.

- Three overlapping ranges.

- Eight non-increasing ranges.


Normal response codes: 200
Error response codes:416,404,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - container: container
   - limit: limit
   - marker: marker
   - end_marker: end_marker
   - prefix: prefix
   - format: format
   - delimiter: delimiter
   - path: path
   - X-Auth-Token: X-Auth-Token
   - X-Newest: X-Newest
   - Accept: Accept
   - X-Container-Meta-Temp-URL-Key: X-Container-Meta-Temp-URL-Key
   - X-Container-Meta-Temp-URL-Key-2: X-Container-Meta-Temp-URL-Key-2
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - X-Container-Meta-name: X-Container-Meta-name
   - Content-Length: Content-Length
   - X-Container-Object-Count: X-Container-Object-Count
   - Accept-Ranges: Accept-Ranges
   - X-Container-Meta-Temp-URL-Key: X-Container-Meta-Temp-URL-Key
   - X-Container-Bytes-Used: X-Container-Bytes-Used
   - X-Container-Meta-Temp-URL-Key-2: X-Container-Meta-Temp-URL-Key-2
   - X-Timestamp: X-Timestamp
   - X-Trans-Id: X-Trans-Id
   - Date: Date
   - Content-Type: Content-Type
   - hash: hash
   - last_modified: last_modified
   - bytes: bytes
   - name: name
   - content_type: content_type




Response Example
----------------

.. literalinclude:: samples/objects-list-http-response-xml.txt
   :language: javascript






