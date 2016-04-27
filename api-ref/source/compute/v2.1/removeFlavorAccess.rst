
Remove flavor access from tenant
================================

.. rest_method::  POST /v2.1/{tenant_id}/flavors/os-flavor-access/{flavor_id}/action

Removes flavor access from a tenant and flavor.

Specify the ``removeTenantAccess`` action and the ``tenant_id`` in
the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - flavor_id: flavor_id

Request Example
---------------

.. literalinclude:: ../samples/os-flavor-access/flavor-access-remove-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-flavor-access/flavor-access-remove-response.json
   :language: javascript



