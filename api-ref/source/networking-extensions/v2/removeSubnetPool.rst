
Delete subnet pool
==================

.. rest_method::  DELETE /v2.0/subnetpools/{subnetpool_id}

Deletes a subnet pool.

The operation fails if any subnets allocated from the subnet pool
are still in use.

Error response codes:404,204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - subnetpool_id: subnetpool_id









