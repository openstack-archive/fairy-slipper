
Show subnet details
===================

.. rest_method::  GET /v2.0/subnets/{subnet_id}

Shows details for a subnet.

Use the fields query parameter to filter the results.


Normal response codes: 200
Error response codes:404,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - subnet_id: subnet_id






Response Example
----------------

.. literalinclude:: ../samples/subnets/subnet-show-response.json
   :language: javascript





