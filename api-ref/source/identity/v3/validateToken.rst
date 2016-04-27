
Validate and show information for token
=======================================

.. rest_method::  GET /v3/auth/tokens

Validates and shows information for a token, including its expiration date and authorization scope.

Pass your own token in the ``X-Auth-Token`` request header.

Pass the token that you want to validate in the ``X-Subject-Token``
request header.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - X-Auth-Token: X-Auth-Token
   - X-Subject-Token: X-Subject-Token



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - X-Subject-Token: X-Subject-Token
   - X-Auth-Token: X-Auth-Token
   - domain: domain
   - methods: methods
   - links: links
   - user: user
   - token: token
   - expires_at: expires_at
   - project: project
   - catalog: catalog
   - extras: extras
   - roles: roles
   - audit_ids: audit_ids
   - issued_at: issued_at
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/auth-token-unscoped-response.json
   :language: javascript










