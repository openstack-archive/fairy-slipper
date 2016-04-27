
Show object metadata
====================

.. rest_method::  HEAD /v1/{account}/{container}/{object}

Shows object metadata.

If the ``Content-Length`` response header is non-zero, the example
cURL command stalls after it prints the response headers because it
is waiting for a response body. However, the Object Storage system
does not return a response body for the HEAD operation.

Example requests and responses:

- Show object metadata:

  ::

     curl -i $publicURL/marktwain/goodbye -X HEAD -H "X-Auth-Token: $token"




  ::

     HTTP/1.1 200 OK
     Content-Length: 14
     Accept-Ranges: bytes
     Last-Modified: Thu, 16 Jan 2014 21:12:31 GMT
     Etag: 451e372e48e0f6b1114fa0724aa79fa1
     X-Timestamp: 1389906751.73463
     X-Object-Meta-Book: GoodbyeColumbus
     Content-Type: application/octet-stream
     X-Trans-Id: tx37ea34dcd1ed48ca9bc7d-0052d84b6f
     Date: Thu, 16 Jan 2014 21:13:19 GMT


If the request succeeds, the operation returns the ``200`` response
code.


Normal response codes: 200
Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - object: object
   - container: container
   - X-Auth-Token: X-Auth-Token
   - temp_url_sig: temp_url_sig
   - temp_url_expires: temp_url_expires
   - filename: filename
   - X-Newest: X-Newest
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Last-Modified: Last-Modified
   - Content-Length: Content-Length
   - X-Object-Meta-name: X-Object-Meta-name
   - Content-Disposition: Content-Disposition
   - Content-Encoding: Content-Encoding
   - X-Delete-At: X-Delete-At
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




