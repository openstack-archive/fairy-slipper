
Resize server (resize action)
=============================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Resizes a server.

Specify the ``resize`` action in the request body.

A successfully resized server shows a ``VERIFY_RESIZE`` status,
``RESIZED`` VM status, and ``finished`` migration status. If you
set the ``resize_confirm_window`` option of the Compute service to
an integer value, the Compute service automatically confirms the
resize operation after the set interval in seconds.

Preconditions

- You can only resize a server when its status is ``ACTIVE`` or
  ``SHUTOFF``.

- If the server is locked, you must have administrator privileges to
  resize the server.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - resize: resize
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/resize-request.json
   :language: javascript
















