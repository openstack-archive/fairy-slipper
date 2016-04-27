
Update tenant
=============

.. rest_method::  POST /v2.0/tenants/{tenantId}

Updates a tenant.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant: tenant
   - enabled: enabled
   - description: description
   - name: name
   - id: id
   - tenantId: tenantId

Request Example
---------------

.. literalinclude:: ../samples/OS-KSADM/tenant-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - tenant: tenant
   - enabled: enabled
   - description: description
   - name: name
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/OS-KSADM/tenant-show-response.json
   :language: javascript












