
Enable host
===========

.. rest_method::  PUT /v2.1/{tenant_id}/os-hosts/{host_name}

Enables or puts a host in maintenance mode.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - host_name: host_name

Request Example
---------------

.. literalinclude:: ../samples/os-hosts/host-update-maintenance-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-hosts/host-update-maintenance-response.json
   :language: javascript



