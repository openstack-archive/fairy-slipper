
Create (allocate) floating IP address
=====================================

.. rest_method::  POST /v2.1/{tenant_id}/os-floating-ips

Creates, or allocates, a floating IP address for the current project. By default, the floating IP address is allocated from the public pool.

If more than one floating IP address pool is available, use the
``pool`` parameter to specify from which pool to allocate the IP
address.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - pool: pool
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-floating-ips/floating-ip-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-floating-ips/floating-ip-create-response.json
   :language: javascript




