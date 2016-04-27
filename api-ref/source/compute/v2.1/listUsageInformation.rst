
List tenant usage for all tenants
=================================

.. rest_method::  GET /v2.1/{tenant_id}/os-simple-tenant-usage

Lists usage information for all tenants.


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

.. literalinclude:: ../samples/os-simple-tenant-usage/simple-tenant-usage-show-general-response.json
   :language: javascript



