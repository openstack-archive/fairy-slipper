
Show tenant details, by ID
==========================

.. rest_method::  GET /v2.0/tenants/{tenantId}

Shows details for a tenant, by ID.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenantId: tenantId






Response Example
----------------

.. literalinclude:: ../samples/admin/tenant-show-response.json
   :language: javascript











