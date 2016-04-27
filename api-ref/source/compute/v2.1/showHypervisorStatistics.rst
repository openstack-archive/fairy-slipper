
Show hypervisor statistics
==========================

.. rest_method::  GET /v2.1/{tenant_id}/os-hypervisors/statistics

Shows summary statistics for all hypervisors over all compute nodes.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-hypervisors/hypervisor-statistics-show-response.json
   :language: javascript



