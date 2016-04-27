
Get object content and metadata
===============================

.. rest_method::  GET /v1/{account}/{container}/{object}

Downloads the object content and gets the object metadata.

This operation returns the object metadata in the response headers
and the object content in the response body.

If this is a large object, the response body contains the
concatenated content of the segment objects. To get the manifest
instead of concatenated segment objects for a static large object,
use the ``multipart-manifest`` query parameter.

Example requests and responses:

- Show object details for the ``goodbye`` object in the
  ``marktwain`` container:

  ::

     curl -i $publicURL/marktwain/goodbye -X GET -H "X-Auth-Token: $token"




  ::

     HTTP/1.1 200 OK
     Content-Length: 14
     Accept-Ranges: bytes
     Last-Modified: Wed, 15 Jan 2014 16:41:49 GMT
     Etag: 451e372e48e0f6b1114fa0724aa79fa1
     X-Timestamp: 1389804109.39027
     X-Object-Meta-Orig-Filename: goodbyeworld.txt
     Content-Type: application/octet-stream
     X-Trans-Id: tx8145a190241f4cf6b05f5-0052d82a34
     Date: Thu, 16 Jan 2014 18:51:32 GMT
     Goodbye World!


- Show object details for the ``goodbye`` object, which does not
  exist, in the ``janeausten`` container:

  ::

     curl -i $publicURL/janeausten/goodbye -X GET -H "X-Auth-Token: $token"




  ::

     HTTP/1.1 404 Not Found
     Content-Length: 70
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx073f7cbb850c4c99934b9-0052d82b04
     Date: Thu, 16 Jan 2014 18:55:00 GMT
     <html>
     <h1>Not Found
     </h1>
     <p>The resource could not be found.
     </p>
     </html>


The operation returns the ``Range Not Satisfiable (416)`` response
code for any ranged GET requests that specify more than:

- Fifty ranges.

- Three overlapping ranges.

- Eight non-increasing ranges.


Normal response codes: 200
Error response codes:416,404,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - object: object
   - container: container
   - X-Auth-Token: X-Auth-Token
   - X-Newest: X-Newest
   - temp_url_sig: temp_url_sig
   - temp_url_expires: temp_url_expires
   - filename: filename
   - multipart-manifest: multipart-manifest
   - Range: Range
   - If-Match: If-Match
   - If-None-Match: If-None-Match
   - If-Modified-Since: If-Modified-Since
   - If-Unmodified-Since: If-Unmodified-Since
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Content-Length: Content-Length
   - X-Object-Meta-name: X-Object-Meta-name
   - Content-Disposition: Content-Disposition
   - Content-Encoding: Content-Encoding
   - X-Delete-At: X-Delete-At
   - Accept-Ranges: Accept-Ranges
   - X-Object-Manifest: X-Object-Manifest
   - Last-Modified: Last-Modified
   - ETag: ETag
   - X-Timestamp: X-Timestamp
   - X-Trans-Id: X-Trans-Id
   - Date: Date
   - X-Static-Large-Object: X-Static-Large-Object
   - Content-Type: Content-Type




Response Example
----------------

.. literalinclude:: 
   :language: javascript





