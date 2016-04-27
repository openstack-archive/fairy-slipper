
Show container metadata
=======================

.. rest_method::  HEAD /v1/{account}/{container}

Shows container metadata, including the number of objects and the total bytes of all objects stored in the container.

Show container metadata request:

::

   curl -i $publicURL/marktwain -X HEAD -H "X-Auth-Token: $token"




::

   HTTP/1.1 204 No Content
   Content-Length: 0
   X-Container-Object-Count: 1
   Accept-Ranges: bytes
   X-Container-Meta-Book: TomSawyer
   X-Timestamp: 1389727543.65372
   X-Container-Meta-Author: SamuelClemens
   X-Container-Bytes-Used: 14
   Content-Type: text/plain; charset=utf-8
   X-Trans-Id: tx0287b982a268461b9ec14-0052d826e2
   Date: Thu, 16 Jan 2014 18:37:22 GMT


If the request succeeds, the operation returns the ``No Content
(204)`` response code.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - container: container
   - X-Auth-Token: X-Auth-Token
   - X-Newest: X-Newest
   - X-Container-Meta-Temp-URL-Key: X-Container-Meta-Temp-URL-Key
   - X-Container-Meta-Temp-URL-Key-2: X-Container-Meta-Temp-URL-Key-2
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - X-Container-Sync-Key: X-Container-Sync-Key
   - X-Container-Meta-name: X-Container-Meta-name
   - Content-Length: Content-Length
   - X-Container-Object-Count: X-Container-Object-Count
   - X-Container-Write: X-Container-Write
   - X-Container-Meta-Quota-Count: X-Container-Meta-Quota-Count
   - Accept-Ranges: Accept-Ranges
   - X-Container-Read: X-Container-Read
   - X-Container-Meta-Access-Control-Expose-Headers: X-Container-Meta-Access-Control-Expose-Headers
   - X-Container-Meta-Temp-URL-Key: X-Container-Meta-Temp-URL-Key
   - X-Container-Bytes-Used: X-Container-Bytes-Used
   - X-Container-Meta-Temp-URL-Key-2: X-Container-Meta-Temp-URL-Key-2
   - X-Timestamp: X-Timestamp
   - X-Container-Meta-Access-Control-Allow-Origin: X-Container-Meta-Access-Control-Allow-Origin
   - X-Container-Meta-Access-Control-Max-Age: X-Container-Meta-Access-Control-Max-Age
   - Date: Date
   - X-Trans-Id: X-Trans-Id
   - X-Container-Sync-To: X-Container-Sync-To
   - Content-Type: Content-Type
   - X-Container-Meta-Quota-Bytes: X-Container-Meta-Quota-Bytes
   - X-Versions-Location: X-Versions-Location





