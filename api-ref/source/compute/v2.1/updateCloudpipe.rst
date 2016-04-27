
Update cloudpipe
================

.. rest_method::  POST /v2.1/{tenant_id}/os-cloudpipe/configure-project

Updates the virtual private network (VPN) IP address and port for a cloudpipe instance.

Error response codes:202,415,405,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - vpn_ip: vpn_ip
   - vpn_port: vpn_port
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-cloudpipe/cloud-pipe-update-request.json
   :language: javascript














