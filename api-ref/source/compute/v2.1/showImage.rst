
Show image details
==================

.. rest_method::  GET /v2.1/{tenant_id}/images/{image_id}

Shows details for an image.


Normal response codes: 200
Error response codes:203,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - image_id: image_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/images/image-show-response.json
   :language: javascript










