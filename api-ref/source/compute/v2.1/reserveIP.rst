
Reserve or release a fixed IP
=============================

.. rest_method::  POST /v2.1/{tenant_id}/os-fixed-ips/{fixed_ip}/action

Reserves or releases a fixed IP.

To reserve a fixed IP address, specify ``reserve`` in the request
body. To release a fixed IP address, specify ``unreserve`` in the
request body.

Error response codes:202,415,405,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - fixed_ip: fixed_ip

Request Example
---------------

.. literalinclude:: ../samples/os-fixed-ips/fixedip-create-request.json
   :language: javascript














