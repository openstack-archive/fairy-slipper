
Show domain configuration
=========================

.. rest_method::  GET /v3/domains/{domain_id}/config

Shows details for a domain configuration.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id



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

.. literalinclude:: ../samples/admin/domain-config-show-response.json
   :language: javascript










