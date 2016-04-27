
Delete quotas
=============

.. rest_method::  DELETE /v2/{tenant_id}/quota-sets/{tenant_id}

Deletes quotas for a tenant. The quota reverts to the default quota.

If you specify the optional ``user_id`` query parameter, you delete
the quotas for this user in the tenant. If you omit this parameter,
you delete the quotas for the project.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id







