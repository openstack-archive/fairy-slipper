
Show domain group option configuration
======================================

.. rest_method::  GET /v3/domains/{domain_id}/config/{group}/{option}

Shows details for a domain group option configuration.

The API supports only the ``identity`` and ``ldap`` groups. For the
``ldap`` group, a valid value is ``url`` or ``user_tree_dn``. For
the ``identity`` group, a valid value is ``driver``.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - group: group
   - option: option



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

.. literalinclude:: ../samples/admin/domain-config-group-option-show-response.json
   :language: javascript










