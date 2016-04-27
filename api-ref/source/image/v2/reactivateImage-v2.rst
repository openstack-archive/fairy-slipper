
Reactivate image
================

.. rest_method::  POST /v2/images/{image_id}/actions/reactivate

(Since Image API v2.0) Reactivates an image.

The reactivate operation returns an error if the image status is
not ``active`` or ``deactivated``.

Preconditions

- The image must exist.

Error response codes:404,204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - image_id: image_id








