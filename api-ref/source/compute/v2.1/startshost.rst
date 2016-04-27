
Start host
==========

.. rest_method::  GET /v2.1/{tenant_id}/os-hosts/{host_name}/startup

Starts a host.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - host_name: host_name



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-hosts/host-start-response.json
   :language: javascript



