
Remove VPN service
==================

.. rest_method::  DELETE /v2.0/vpn/vpnservices/{service_id}

Removes a VPN service.

If the service has connections, the request is rejected.

Error response codes:409,404,204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_id: service_id










