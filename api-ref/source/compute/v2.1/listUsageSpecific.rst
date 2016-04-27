
Show usage details for tenant
=============================

.. rest_method::  GET /v2.1/{tenant_id}/os-simple-tenant-usage/{tenant_id}

Shows usage details for a tenant.


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

.. literalinclude:: ../samples/os-simple-tenant-usage/simple-tenant-usage-show-response.json
   :language: javascript



