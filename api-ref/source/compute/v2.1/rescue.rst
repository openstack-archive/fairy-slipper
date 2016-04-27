
Rescue server (rescue action)
=============================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Puts a server in rescue mode and changes its status to ``RESCUE``.

Specify the ``rescue`` action in the request body.

If you specify the ``rescue_image_ref`` extended attribute, the
image is used to rescue the instance. If you omit an image
reference, the base image reference is used by default.

Asynchronous Postconditions

- After you successfully rescue a server and make a ``GET
  /v2.1/​{tenant_id}​/servers/​{server_id}​`` request, its status
  changes to ``RESCUE``.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - rescue_image_ref: rescue_image_ref
   - rescue: rescue
   - adminPass: adminPass
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/rescue-with-image-ref-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - adminPass: adminPass





