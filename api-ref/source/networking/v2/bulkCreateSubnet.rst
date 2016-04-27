
Bulk create subnet
==================

.. rest_method::  POST /v2.0/subnets

Creates multiple subnets in a single request. Specify a list of subnets in the request body.

The bulk create operation is always atomic. Either all or no
subnets in the request body are created.

Error response codes:201,404,403,401,400,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/subnets/subnets-create-bulk-request.json
   :language: javascript













