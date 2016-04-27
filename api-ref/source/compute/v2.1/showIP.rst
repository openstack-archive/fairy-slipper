
Show fixed IP details
=====================

.. rest_method::  GET /v2.1/{tenant_id}/os-fixed-ips/{fixed_ip}

Shows details for a fixed IP address.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - fixed_ip: fixed_ip






Response Example
----------------

.. literalinclude:: ../samples/os-fixed-ips/fixedip-show-response.json
   :language: javascript









