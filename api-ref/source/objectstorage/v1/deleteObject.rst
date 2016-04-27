
Delete object
=============

.. rest_method::  DELETE /v1/{account}/{container}/{object}

Permanently deletes an object from the object store.

You can use the COPY method to copy the object to a new location.
Then, use the DELETE method to delete the original object.

Object deletion occurs immediately at request time. Any subsequent
GET , HEAD , POST , or DELETE operations return a ``404 Not Found``
error code.

For static large object manifests, you can add the ``?multipart-
manifest=delete`` query parameter. This operation deletes the
segment objects and if all deletions succeed, this operation
deletes the manifest object.

Example request and response:

- Delete the ``helloworld`` object from the ``marktwain`` container:

  ::

     curl -i $publicURL/marktwain/helloworld -X DELETE -H "X-Auth-Token: $token"




  ::

     HTTP/1.1 204 No Content
     Content-Length: 0
     Content-Type: text/html; charset=UTF-8
     X-Trans-Id: tx36c7606fcd1843f59167c-0052d6fdac
     Date: Wed, 15 Jan 2014 21:29:16 GMT


Typically, the DELETE operation does not return a response body.
However, with the ``multipart-manifest=delete`` query parameter,
the response body contains a list of manifest and segment objects
and the status of their DELETE operations.

Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - object: object
   - container: container
   - multipart-manifest: multipart-manifest
   - X-Auth-Token: X-Auth-Token
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Date: Date
   - X-Timestamp: X-Timestamp
   - Content-Length: Content-Length
   - Content-Type: Content-Type
   - X-Trans-Id: X-Trans-Id





