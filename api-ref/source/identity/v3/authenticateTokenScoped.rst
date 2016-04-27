
Token authentication with scoped authorization
==============================================

.. rest_method::  POST /v3/auth/tokens

Authenticates an identity and generates a token. Uses the token authentication method and scopes authorization to a project or domain.

In the request body, provide the token ID and the ``project`` or
``domain`` authorization scope.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - methods: methods
   - auth: auth
   - token: token
   - audit_ids: audit_ids
   - scope: scope
   - id: id
   - identity: identity
   - nocatalog: nocatalog

Request Example
---------------

.. literalinclude:: ../samples/admin/auth-token-scoped-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - X-Subject-Token: X-Subject-Token
   - X-Auth-Token: X-Auth-Token














