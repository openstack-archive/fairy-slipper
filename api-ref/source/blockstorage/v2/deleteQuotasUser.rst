
Delete quotas for user
======================

.. rest_method::  DELETE /v2/{admin_tenant_id}/os-quota-sets/{tenant_id}/{user_id}

Deletes quotas for a user so that the quotas revert to default values.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - user_id: user_id
   - admin_tenant_id: admin_tenant_id






Response Example
----------------

.. literalinclude:: 
   :language: javascript



