
Delete floating IP
==================

.. rest_method::  DELETE /v2.0/floatingips/{floatingip_id}

Deletes a floating IP and, if present, its associated port.

This example deletes a floating IP:

::

   DELETE /v2.0/floatingips/{floatingip_id} Accept: application/json

Error response codes:404,204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - floatingip_id: floatingip_id









