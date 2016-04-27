
Delete domain group option configuration
========================================

.. rest_method::  DELETE /v3/domains/{domain_id}/config/{group}/{option}

Deletes a domain group option configuration.

The API supports only the ``identity`` and ``ldap`` groups. For the
``ldap`` group, a valid value is ``url`` or ``user_tree_dn``. For
the ``identity`` group, a valid value is ``driver``.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - group: group
   - option: option
















