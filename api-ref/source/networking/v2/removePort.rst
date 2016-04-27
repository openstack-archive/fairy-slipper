
Delete port
===========

.. rest_method::  DELETE /v2.0/ports/{port_id}

Deletes a port.

Any IP addresses that are associated with the port are returned to
the respective subnets allocation pools.

Error response codes:404,403,204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - port_id: port_id










