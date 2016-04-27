
Delete subnet
=============

.. rest_method::  DELETE /v2.0/subnets/{subnet_id}

Deletes a subnet.

The operation fails if subnet IP addresses are still allocated.

Error response codes:409,404,204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - subnet_id: subnet_id










