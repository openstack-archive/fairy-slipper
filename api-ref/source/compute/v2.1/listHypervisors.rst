
List hypervisors
================

.. rest_method::  GET /v2.1/{tenant_id}/os-hypervisors

Lists hypervisors.


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

.. literalinclude:: ../samples/os-hypervisors/hypervisors-list-response.json
   :language: javascript



