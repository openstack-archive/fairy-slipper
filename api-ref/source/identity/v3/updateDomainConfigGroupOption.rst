
Update domain group option configuration
========================================

.. rest_method::  PATCH /v3/domains/{domain_id}/config/{group}/{option}

Updates a domain group option configuration.

The API supports only the ``identity`` and ``ldap`` groups. For the
``ldap`` group, a valid value is ``url`` or ``user_tree_dn``. For
the ``identity`` group, a valid value is ``driver``.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - url: url
   - driver: driver
   - ldap: ldap
   - config: config
   - user_tree_dn: user_tree_dn
   - identity: identity
   - domain_id: domain_id
   - group: group
   - option: option

Request Example
---------------

.. literalinclude:: ../samples/admin/domain-config-group-option-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - url: url
   - driver: driver
   - ldap: ldap
   - config: config
   - user_tree_dn: user_tree_dn
   - identity: identity




Response Example
----------------

.. literalinclude:: ../samples/admin/domain-config-group-option-update-response.json
   :language: javascript












