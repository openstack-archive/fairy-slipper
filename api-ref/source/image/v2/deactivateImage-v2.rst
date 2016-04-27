
Deactivate image
================

.. rest_method::  POST /v2/images/{image_id}/actions/deactivate

(Since Image API v2.0) Deactivates an image.

If you try to download a deactivated image, the call returns the
``Forbidden (403)`` response code. Also, only administrative users
can view image locations for deactivated images.

The deactivate operation returns an error if the image status is
not ``active`` or ``deactivated``.

Preconditions

- The image must exist.

Error response codes:404,403,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - image_id: image_id









