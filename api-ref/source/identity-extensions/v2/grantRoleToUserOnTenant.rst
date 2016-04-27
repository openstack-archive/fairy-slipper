
Grant roles to user on tenant
=============================

.. rest_method::  PUT /v2.0/tenants/{tenantId}/users/{userId}/roles/OS-KSADM/{roleId}

Grants a role to a user for a tenant.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - userId: userId
   - roleId: roleId
   - tenantId: tenantId
















