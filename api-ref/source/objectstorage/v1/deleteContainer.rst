
Delete container
================

.. rest_method::  DELETE /v1/{account}/{container}

Deletes an empty container.

This operation fails unless the container is empty. An empty
container has no objects.

Delete the ``steven`` container:

::

   curl -i $publicURL/steven -X DELETE -H "X-Auth-Token: $token"


If the container does not exist, the response is:

::

   HTTP/1.1 404 Not Found
   Content-Length: 70
   Content-Type: text/html; charset=UTF-8
   X-Trans-Id: tx4d728126b17b43b598bf7-0052d81e34
   Date: Thu, 16 Jan 2014 18:00:20 GMT


If the container exists and the deletion succeeds, the response is:

::

   HTTP/1.1 204 No Content
   Content-Length: 0
   Content-Type: text/html; charset=UTF-8
   X-Trans-Id: txf76c375ebece4df19c84c-0052d81f14
   Date: Thu, 16 Jan 2014 18:04:04 GMT


If the container exists but is not empty, the response is:

::

   HTTP/1.1 409 Conflict
   Content-Length: 95
   Content-Type: text/html; charset=UTF-8
   X-Trans-Id: tx7782dc6a97b94a46956b5-0052d81f6b
   Date: Thu, 16 Jan 2014 18:05:31 GMT
   <html>
   <h1>Conflict
   </h1>
   <p>There was a conflict when trying to complete your request.
   </p>
   </html>

Error response codes:404,204,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - container: container
   - X-Auth-Token: X-Auth-Token
   - X-Container-Meta-Temp-URL-Key: X-Container-Meta-Temp-URL-Key
   - X-Container-Meta-Temp-URL-Key-2: X-Container-Meta-Temp-URL-Key-2
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Date: Date
   - X-Timestamp: X-Timestamp
   - Content-Length: Content-Length
   - Content-Type: Content-Type
   - X-Trans-Id: X-Trans-Id







