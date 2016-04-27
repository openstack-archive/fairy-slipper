
Copy object
===========

.. rest_method::  COPY /v1/{account}/{container}/{object}

Copies an object to another object in the object store.

You can copy an object to a new object with the same name. Copying
to the same name is an alternative to using POST to add metadata to
an object. With POST , you must specify all the metadata. With COPY
, you can add additional metadata to the object.

With COPY , you can set the ``X-Fresh-Metadata`` header to ``true``
to copy the object without any existing metadata.

Alternatively, you can use PUT with the ``X-Copy-From`` request
header to accomplish the same operation as the COPY object
operation.

The PUT operation always creates an object. If you use this
operation on an existing object, you replace the existing object
and metadata rather than modifying the object. Consequently, this
operation returns the ``Created (201)`` response code.

If you use this operation to copy a manifest object, the new object
is a normal object and not a copy of the manifest. Instead it is a
concatenation of all the segment objects. This means that you
cannot copy objects larger than 5 GB in size. All metadata is
preserved during the object copy. If you specify metadata on the
request to copy the object, either PUT or COPY , the metadata
overwrites any conflicting keys on the target (new) object.

Example requests and responses:

- Copy the ``goodbye`` object from the ``marktwain`` container to
  the ``janeausten`` container:

  ::

     curl -i $publicURL/marktwain/goodbye -X COPY -H "X-Auth-Token: $token" -H "Destination: janeausten/goodbye"




  ::

     HTTP/1.1 201 Created
     Content-Length: 0
     X-Copied-From-Last-Modified: Thu, 16 Jan 2014 21:19:45 GMT
     X-Copied-From: marktwain/goodbye
     Last-Modified: Fri, 17 Jan 2014 18:22:57 GMT
     Etag: 451e372e48e0f6b1114fa0724aa79fa1
     Content-Type: text/html; charset=UTF-8
     X-Object-Meta-Movie: AmericanPie
     X-Trans-Id: txdcb481ad49d24e9a81107-0052d97501
     Date: Fri, 17 Jan 2014 18:22:57 GMT


- Alternatively, you can use PUT to copy the ``goodbye`` object from
  the ``marktwain`` container to the ``janeausten`` container. This
  request requires a ``Content-Length`` header, even if it is set
  to zero (0).

  ::

     curl -i $publicURL/janeausten/goodbye -X PUT -H "X-Auth-Token: $token" -H "X-Copy-From: /marktwain/goodbye" -H "Content-Length: 0"




  ::

     HTTP/1.1 201 Created
     Content-Length: 0
     X-Copied-From-Last-Modified: Thu, 16 Jan 2014 21:19:45 GMT
     X-Copied-From: marktwain/goodbye
     Last-Modified: Fri, 17 Jan 2014 18:22:57 GMT
     Etag: 451e372e48e0f6b1114fa0724aa79fa1
     Content-Type: text/html; charset=UTF-8
     X-Object-Meta-Movie: AmericanPie
     X-Trans-Id: txdcb481ad49d24e9a81107-0052d97501
     Date: Fri, 17 Jan 2014 18:22:57 GMT


When several replicas exist, the system copies from the most recent
replica. That is, the COPY operation behaves as though the
``X-Newest`` header is in the request.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - object: object
   - container: container
   - X-Auth-Token: X-Auth-Token
   - Destination: Destination
   - Content-Type: Content-Type
   - Content-Encoding: Content-Encoding
   - Content-Disposition: Content-Disposition
   - X-Object-Meta-name: X-Object-Meta-name
   - X-Fresh-Metadata: X-Fresh-Metadata
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Content-Length: Content-Length
   - X-Object-Meta-name: X-Object-Meta-name
   - X-Copied-From-Last-Modified: X-Copied-From-Last-Modified
   - X-Copied-From: X-Copied-From
   - Last-Modified: Last-Modified
   - ETag: ETag
   - X-Timestamp: X-Timestamp
   - X-Trans-Id: X-Trans-Id
   - Date: Date
   - Content-Type: Content-Type





