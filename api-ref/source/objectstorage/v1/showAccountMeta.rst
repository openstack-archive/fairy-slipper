
Show account metadata
=====================

.. rest_method::  HEAD /v1/{account}

Shows metadata for an account.

Metadata for the account includes:

- Number of containers

- Number of objects

- Total number of bytes that are stored in Object Storage for the
  account

Because the storage system can store large amounts of data, take
care when you represent the total bytes response as an integer;
when possible, convert it to a 64-bit unsigned integer if your
platform supports that primitive type.

Do not include metadata headers in this request.

Show account metadata request:

::

   curl -i $publicURL -X HEAD -H "X-Auth-Token: $token"




::

   HTTP/1.1 204 No Content
   Content-Length: 0
   X-Account-Object-Count: 1
   X-Account-Meta-Book: MobyDick
   X-Timestamp: 1389453423.35964
   X-Account-Bytes-Used: 14
   X-Account-Container-Count: 2
   Content-Type: text/plain; charset=utf-8
   Accept-Ranges: bytes
   X-Trans-Id: txafb3504870144b8ca40f7-0052d955d4
   Date: Fri, 17 Jan 2014 16:09:56 GMT


If the account or authentication token is not valid, the operation
returns the ``Unauthorized (401)`` response code.

Error response codes:204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - X-Auth-Token: X-Auth-Token
   - X-Newest: X-Newest
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Content-Length: Content-Length
   - X-Account-Meta-name: X-Account-Meta-name
   - X-Account-Object-Count: X-Account-Object-Count
   - X-Account-Meta-Temp-URL-Key-2: X-Account-Meta-Temp-URL-Key-2
   - X-Timestamp: X-Timestamp
   - X-Account-Meta-Temp-URL-Key: X-Account-Meta-Temp-URL-Key
   - X-Trans-Id: X-Trans-Id
   - Date: Date
   - X-Account-Bytes-Used: X-Account-Bytes-Used
   - X-Account-Container-Count: X-Account-Container-Count
   - Content-Type: Content-Type






