
List users on a tenant
======================

.. rest_method::  GET /v2.0/tenants/{tenantId}/users

Lists all users for a tenant.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenantId: tenantId






Response Example
----------------

.. literalinclude:: ../samples/OS-KSADM/users-list-response.json
   :language: javascript











