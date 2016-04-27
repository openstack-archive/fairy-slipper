
Download binary image data
==========================

.. rest_method::  GET /v2/images/{image_id}/file

(Since Image API v2.0) Downloads binary image data.

Example call: ``curl -i -X GET -H "X-Auth-Token: $token"
$image_url/v2/images/{image_id}/file``

The response body contains the raw binary data that represents the
actual virtual disk. The ``Content-Type`` header contains the
``application/octet-stream`` value. The ``Content-MD5`` header
contains an MD5 checksum of the image data. Use this checksum to
verify the integrity of the image data.



Preconditions

- The images must exist.

Synchronous Postconditions

- You can download the binary image data in your machine if the
  image has image data.

- If image data exists, the call returns the HTTP ``200`` response
  code.

- If no image data exists, the call returns the HTTP ``204``
  response code.


Normal response codes: 200
Error response codes:404,403,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - image_id: image_id
   - Content-Range: Content-Range






Response Example
----------------

.. literalinclude:: 
   :language: javascript






