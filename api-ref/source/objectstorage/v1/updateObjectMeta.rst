
Create or update object metadata
================================

.. rest_method::  POST /v1/{account}/{container}/{object}

Creates or updates object metadata.

To create or update custom metadata, use the ``X-Object-
Meta-{name}`` header, where ``{name}`` is the name of the metadata
item.

In addition to the custom metadata, you can update the ``Content-
Type``, ``Content-Encoding``, ``Content-Disposition``, and ``X
-Delete-At`` system metadata items. However you cannot update other
system metadata, such as ``Content-Length`` or ``Last-Modified``.

You can use COPY as an alternate to the POST operation by copying
to the same object. With the POST operation you must specify all
metadata items, whereas with the COPY operation, you need to
specify only changed or additional items.

All metadata is preserved during the object copy. If you specify
metadata on the request to copy the object, either PUT or COPY ,
the metadata overwrites any conflicting keys on the target (new)
object.

A POST request deletes any existing custom metadata that you added
with a previous PUT or POST request. Consequently, you must specify
all custom metadata in the request. However, system metadata is
unchanged by the POST request unless you explicitly supply it in a
request header.

You can also set the ``X-Delete-At`` or ``X-Delete-After`` header
to define when to expire the object.

When used as described in this section, the POST operation creates
or replaces metadata. This form of the operation has no request
body.

You can also use the `form POST feature
<http://docs.openstack.org/liberty/config-reference/content/object-
storage-form-post.html>`_ to upload objects.

Example requests and responses:

- Create object metadata:

  ::

     curl -i $publicURL/marktwain/goodbye -X POST -H "X-Auth-Token: $token" -H "X-Object-Meta-Book: GoodbyeColumbus"




  ::

     HTTP/1.1 202 Accepted
     Content-Length: 76
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: txb5fb5c91ba1f4f37bb648-0052d84b3f
     Date: Thu, 16 Jan 2014 21:12:31 GMT
     <html>
     <h1>Accepted
     </h1>
     <p>The request is accepted for processing.
     </p>
     </html>


- Update object metadata:

  ::

     curl -i $publicURL/marktwain/goodbye -X POST -H "X-Auth-Token: $token" H "X-Object-Meta-Book: GoodbyeOldFriend"




  ::

     HTTP/1.1 202 Accepted
     Content-Length: 76
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx5ec7ab81cdb34ced887c8-0052d84ca4
     Date: Thu, 16 Jan 2014 21:18:28 GMT
     <html>
     <h1>Accepted
     </h1>
     <p>The request is accepted for processing.
     </p>
     </html>

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - object: object
   - container: container
   - X-Auth-Token: X-Auth-Token
   - X-Object-Meta-name: X-Object-Meta-name
   - X-Delete-At: X-Delete-At
   - Content-Disposition: Content-Disposition
   - Content-Encoding: Content-Encoding
   - X-Delete-After: X-Delete-After
   - Content-Type: Content-Type
   - X-Detect-Content-Type: X-Detect-Content-Type
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Date: Date
   - X-Timestamp: X-Timestamp
   - Content-Length: Content-Length
   - Content-Type: Content-Type
   - X-Trans-Id: X-Trans-Id





