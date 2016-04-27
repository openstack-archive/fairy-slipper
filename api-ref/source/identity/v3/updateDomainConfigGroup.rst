
Update domain group configuration
=================================

.. rest_method::  PATCH /v3/domains/{domain_id}/config/{group}

Updates a domain group configuration.

The API supports only the ``identity`` and ``ldap`` groups. If you
try to set configuration options for other groups, this call fails
with the ``Forbidden (403)`` response code.


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

Request Example
---------------

.. literalinclude:: ../samples/admin/domain-config-group-update-request.json
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

.. literalinclude:: ../samples/admin/domain-config-group-update-response.json
   :language: javascript












