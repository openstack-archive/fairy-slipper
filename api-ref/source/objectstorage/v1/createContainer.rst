
Create container
================

.. rest_method::  PUT /v1/{account}/{container}

Creates a container.

You do not need to check whether a container already exists before
issuing a PUT operation because the operation is idempotent: It
creates a container or updates an existing container, as
appropriate.

Example requests and responses:

- Create a container with no metadata:

  ::

     curl -i $publicURL/steven -X PUT -H "Content-Length: 0" -H "X-Auth-Token: $token"




  ::

     HTTP/1.1 201 Created
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx7f6b7fa09bc2443a94df0-0052d58b56
     Date: Tue, 14 Jan 2014 19:09:10 GMT


- Create a container with metadata:

  ::

     curl -i $publicURL/marktwain -X PUT -H "X-Auth-Token: $token" -H "X-Container-Meta-Book: TomSawyer"




  ::

     HTTP/1.1 201 Created
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx06021f10fc8642b2901e7-0052d58f37
     Date: Tue, 14 Jan 2014 19:25:43 GMT

Error response codes:201,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - container: container
   - X-Auth-Token: X-Auth-Token
   - X-Container-Read: X-Container-Read
   - X-Container-Write: X-Container-Write
   - X-Container-Sync-To: X-Container-Sync-To
   - X-Container-Sync-Key: X-Container-Sync-Key
   - X-Versions-Location: X-Versions-Location
   - X-Container-Meta-name: X-Container-Meta-name
   - X-Container-Meta-Access-Control-Allow-Origin: X-Container-Meta-Access-Control-Allow-Origin
   - X-Container-Meta-Access-Control-Max-Age: X-Container-Meta-Access-Control-Max-Age
   - X-Container-Meta-Access-Control-Expose-Headers: X-Container-Meta-Access-Control-Expose-Headers
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






