
Update subnet
=============

.. rest_method::  PUT /v2.0/subnets/{subnet_id}

Updates a subnet.

Some attributes, such as IP version (ip_version), and CIDR (cidr)
cannot be updated. Attempting to update these attributes results in
a ``400 Bad Request`` error.


Normal response codes: 200
Error response codes:404,403,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - subnet_id: subnet_id

Request Example
---------------

.. literalinclude:: ../samples/subnets/subnet-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/subnets/subnet-update-response.json
   :language: javascript







