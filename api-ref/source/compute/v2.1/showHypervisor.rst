
Show hypervisor details
=======================

.. rest_method::  GET /v2.1/{tenant_id}/os-hypervisors/{hypervisor_id}

Shows details for a hypervisor.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - hypervisor_id: hypervisor_id
   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-hypervisors/hypervisor-show-response.json
   :language: javascript



