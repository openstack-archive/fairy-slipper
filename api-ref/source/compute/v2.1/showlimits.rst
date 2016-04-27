
Show rate and absolute limits
=============================

.. rest_method::  GET /v2.1/{tenant_id}/limits

Shows rate and absolute limits for the tenant.


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

.. literalinclude:: ../samples/limits/limits-get-response.json
   :language: javascript



