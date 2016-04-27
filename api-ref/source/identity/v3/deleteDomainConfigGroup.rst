
Delete domain group configuration
=================================

.. rest_method::  DELETE /v3/domains/{domain_id}/config/{group}

Deletes a domain group configuration.

The API supports only the ``identity`` and ``ldap`` groups.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - group: group
















