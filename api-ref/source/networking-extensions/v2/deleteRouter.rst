
Delete router
=============

.. rest_method::  DELETE /v2.0/routers/{router_id}

Deletes a logical router and, if present, its external gateway interface.

This operation fails if the router has attached interfaces.

Use the remove router interface operation to remove all router
interfaces before you delete the router.

This example deletes a router:

::

   DELETE /v2.0/routers/{router_id} Accept: application/json

Error response codes:409,404,204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router_id: router_id










