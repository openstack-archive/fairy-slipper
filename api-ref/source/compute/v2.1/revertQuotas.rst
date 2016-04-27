
Revert quotas to defaults
=========================

.. rest_method::  DELETE /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}

Reverts the quotas to default values for a project or a project and a user.

To revert quotas for a project and a user, specify the ``user_id``
query parameter.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - admin_tenant_id: admin_tenant_id







