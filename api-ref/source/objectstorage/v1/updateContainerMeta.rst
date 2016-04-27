
Create, update, or delete container metadata
============================================

.. rest_method::  POST /v1/{account}/{container}

Creates, updates, or deletes custom metadata for a container.

To create, update, or delete a custom metadata item, use the ``X
-Container-Meta-{name}`` header, where ``{name}`` is the name of
the metadata item.

Subsequent requests for the same key and value pair overwrite the
previous value.

To delete container metadata, send an empty value for that header,
such as for the ``X-Container-Meta-Book`` header. If the tool you
use to communicate with Object Storage, such as an older version of
cURL, does not support empty headers, send the ``X-Remove-
Container-Meta-{name}`` header with an arbitrary value. For
example, ``X-Remove-Container-Meta-Book: x``. The operation ignores
the arbitrary value.

If the container already has other custom metadata items, a request
to create, update, or delete metadata does not affect those items.

Example requests and responses:

- Create container metadata:

  ::

     curl -i $publicURL/marktwain -X POST -H "X-Auth-Token: $token" -H "X-Container-Meta-Author: MarkTwain" -H "X-Container-Meta-Web-Directory-Type: text/directory" -H "X-Container-Meta-Century: Nineteenth"




  ::

     HTTP/1.1 204 No Content
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx05dbd434c651429193139-0052d82635
     Date: Thu, 16 Jan 2014 18:34:29 GMT


- Update container metadata:

  ::

     curl -i $publicURL/marktwain -X POST -H "X-Auth-Token: $token" -H "X-Container-Meta-Author: SamuelClemens"




  ::

     HTTP/1.1 204 No Content
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: txe60c7314bf614bb39dfe4-0052d82653
     Date: Thu, 16 Jan 2014 18:34:59 GMT


- Delete container metadata:

  ::

     curl -i $publicURL/marktwain -X POST -H "X-Auth-Token: $token" -H "X-Remove-Container-Meta-Century: x"




  ::

     HTTP/1.1 204 No Content
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx7997e18da2a34a9e84ceb-0052d826d0
     Date: Thu, 16 Jan 2014 18:37:04 GMT


If the request succeeds, the operation returns the ``No Content
(204)`` response code.

To confirm your changes, issue a show container metadata request.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - container: container
   - X-Auth-Token: X-Auth-Token
   - X-Container-Read: X-Container-Read
   - X-Remove-Container-name: X-Remove-Container-name
   - X-Container-Write: X-Container-Write
   - X-Container-Sync-To: X-Container-Sync-To
   - X-Container-Sync-Key: X-Container-Sync-Key
   - X-Versions-Location: X-Versions-Location
   - X-Remove-Versions-Location: X-Remove-Versions-Location
   - X-Container-Meta-name: X-Container-Meta-name
   - X-Container-Meta-Access-Control-Allow-Origin: X-Container-Meta-Access-Control-Allow-Origin
   - X-Container-Meta-Access-Control-Max-Age: X-Container-Meta-Access-Control-Max-Age
   - X-Container-Meta-Access-Control-Expose-Headers: X-Container-Meta-Access-Control-Expose-Headers
   - X-Container-Meta-Quota-Bytes: X-Container-Meta-Quota-Bytes
   - X-Container-Meta-Quota-Count: X-Container-Meta-Quota-Count
   - X-Container-Meta-Web-Directory-Type: X-Container-Meta-Web-Directory-Type
   - Content-Type: Content-Type
   - X-Detect-Content-Type: X-Detect-Content-Type
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





