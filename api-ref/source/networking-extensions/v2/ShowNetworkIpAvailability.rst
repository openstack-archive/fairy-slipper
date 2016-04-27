
Network IP Availability
=======================

.. rest_method::  GET /v2.0/network-ip-availabilities

Show network IP availability of all networks.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - used_ips: used_ips
   - name: name
   - subnet_ip_availability: subnet_ip_availability
   - subnet_id: subnet_id
   - tenant_id: tenant_id
   - id: id
   - ip_version: ip_version
   - cidr: cidr
   - total_ips: total_ips
   - network_ip_availabilities: network_ip_availabilities




Response Example
----------------

.. literalinclude:: ../samples/network-ip-availability/network-ip-availability-show.json
   :language: javascript





