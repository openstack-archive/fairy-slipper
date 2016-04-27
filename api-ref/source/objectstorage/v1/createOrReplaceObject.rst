
Create or replace object
========================

.. rest_method::  PUT /v1/{account}/{container}/{object}

Creates an object with data content and metadata, or replaces an existing object with data content and metadata.

The PUT operation always creates an object. If you use this
operation on an existing object, you replace the existing object
and metadata rather than modifying the object. Consequently, this
operation returns the ``Created (201)`` response code.

If you use this operation to copy a manifest object, the new object
is a normal object and not a copy of the manifest. Instead it is a
concatenation of all the segment objects. This means that you
cannot copy objects larger than 5 GB.

Example requests and responses:

- Create object:

  ::

     curl -i $publicURL/janeausten/helloworld.txt -X PUT -H "Content-Length: 1" -H "Content-Type: text/html; charset=UTF-8" -H "X-Auth-Token: $token"




  ::

     HTTP/1.1 201 Created
     Last-Modified: Fri, 17 Jan 2014 17:28:35 GMT
     Content-Length: 116
     Etag: d41d8cd98f00b204e9800998ecf8427e
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx4d5e4f06d357462bb732f-0052d96843
     Date: Fri, 17 Jan 2014 17:28:35 GMT


- Replace object:

  ::

     curl -i $publicURL/janeausten/helloworld -X PUT -H "Content-Length: 0" -H "X-Auth-Token: $token"




  ::

     HTTP/1.1 201 Created
     Last-Modified: Fri, 17 Jan 2014 17:28:35 GMT
     Content-Length: 116
     Etag: d41d8cd98f00b204e9800998ecf8427e
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx4d5e4f06d357462bb732f-0052d96843
     Date: Fri, 17 Jan 2014 17:28:35 GMT


The ``Created (201)`` response code indicates a successful write.

If the request times out, the operation returns the ``Request
Timeout (408)`` response code.

The ``Length Required (411)`` response code indicates a missing
``Transfer-Encoding`` or ``Content-Length`` request header.

If the MD5 checksum of the data that is written to the object store
does not match the optional ``ETag`` value, the operation returns
the ``Unprocessable Entity (422)`` response code.

Error response codes:201,422,411,408,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - object: object
   - container: container
   - multipart-manifest: multipart-manifest
   - temp_url_sig: temp_url_sig
   - temp_url_expires: temp_url_expires
   - filename: filename
   - X-Object-Manifest: X-Object-Manifest
   - X-Auth-Token: X-Auth-Token
   - Content-Length: Content-Length
   - Transfer-Encoding: Transfer-Encoding
   - Content-Type: Content-Type
   - X-Detect-Content-Type: X-Detect-Content-Type
   - X-Copy-From: X-Copy-From
   - ETag: ETag
   - Content-Disposition: Content-Disposition
   - Content-Encoding: Content-Encoding
   - X-Delete-At: X-Delete-At
   - X-Delete-After: X-Delete-After
   - X-Object-Meta-name: X-Object-Meta-name
   - If-None-Match: If-None-Match
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Content-Length: Content-Length
   - ETag: ETag
   - X-Timestamp: X-Timestamp
   - X-Trans-Id: X-Trans-Id
   - Date: Date
   - Content-Type: Content-Type
   - last_modified: last_modified








