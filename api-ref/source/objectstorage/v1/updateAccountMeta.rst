
Create, update, or delete account metadata
==========================================

.. rest_method::  POST /v1/{account}

Creates, updates, or deletes account metadata.

To create, update, or delete metadata, use the ``X-Account-
Meta-{name}`` request header, where ``{name}`` is the name of the
metadata item.

Subsequent requests for the same key and value pair overwrite the
existing value.

To delete a metadata header, send an empty value for that header,
such as for the ``X-Account-Meta-Book`` header. If the tool you use
to communicate with Object Storage, such as an older version of
cURL, does not support empty headers, send the ``X-Remove-Account-
Meta-{name}`` header with an arbitrary value. For example, ``X
-Remove-Account-Meta-Book: x``. The operation ignores the arbitrary
value.

If the container already has other custom metadata items, a request
to create, update, or delete metadata does not affect those items.

This operation does not accept a request body.

Example requests and responses:

- Create account metadata:

  ::

     curl -i $publicURL -X POST -H "X-Auth-Token: $token" -H "X-Account-Meta-Book: MobyDick" -H "X-Account-Meta-Subject: Literature"




  ::

     HTTP/1.1 204 No Content
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx8c2dd6aee35442a4a5646-0052d954fb
     Date: Fri, 17 Jan 2014 16:06:19 GMT


- Update account metadata:

  ::

     curl -i $publicURL -X POST -H "X-Auth-Token: $token" -H "X-Account-Meta-Subject: AmericanLiterature"




  ::

     HTTP/1.1 204 No Content
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx1439b96137364ab581156-0052d95532
     Date: Fri, 17 Jan 2014 16:07:14 GMT


- Delete account metadata:

  ::

     curl -i $publicURL -X POST -H "X-Auth-Token: $token" -H "X-Remove-Account-Meta-Subject: x"




  ::

     HTTP/1.1 204 No Content
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx411cf57701424da99948a-0052d9556f
     Date: Fri, 17 Jan 2014 16:08:15 GMT


If the request succeeds, the operation returns the ``No Content
(204)`` response code.

To confirm your changes, issue a show account metadata request.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - X-Auth-Token: X-Auth-Token
   - X-Account-Meta-Temp-URL-Key: X-Account-Meta-Temp-URL-Key
   - X-Account-Meta-Temp-URL-Key-2: X-Account-Meta-Temp-URL-Key-2
   - X-Account-Meta-name: X-Account-Meta-name
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





