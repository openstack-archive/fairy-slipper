
Revoke role from user on tenant
===============================

.. rest_method::  DELETE /v2.0/tenants/{tenantId}/users/{userId}/roles/OS-KSADM/{roleId}

Revokes a role from a user for a tenant.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - userId: userId
   - roleId: roleId
   - tenantId: tenantId
















